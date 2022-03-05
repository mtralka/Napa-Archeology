import json
import logging
import tempfile

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import pdfminer
from pdfminer.high_level import extract_pages
import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    id = str(event["id"])
    URL: str = "https://gis.napa.ca.gov/SQLReportGen/Report.ashx?ReportPath=/GIS%20Reports/Parcel_Summary_Report&opts=ASMT|{}"
    bucket: str = "archeo-results"

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("archeo-results")

    response = table.query(KeyConditionExpression=Key("id").eq(str(id)))

    if response["Count"] > 0:
        logger.debug("Exists already", id)
        return {"statusCode": 200, "status": "success"}

    response = requests.get(URL.format(id))

    if response.status_code != 200:
        logger.error(f"Failed {id} - {response.status_code}")
        return {"statusCode": 400, "status": "Error"}

    if not response.content:
        logger.error("No content")
        return {"statusCode": 400, "status": "Error"}

    with tempfile.NamedTemporaryFile() as f:
        f.write(response.content)

        s3_client = boto3.client("s3")
        object_name: str = f"{id}.pdf"

        try:
            response = s3_client.upload_file(f.name, bucket, object_name)
            logger.info(f"Uploaded {object_name}")
        except ClientError as e:
            logger.error(e)

        target = None
        for page_layout in extract_pages(f.name):

            for element in page_layout:
                if str(element.x0) != "214.344" and str(element.x0) != "214.344":
                    continue

                if str(element.y0) != "225.161207" and str(element.y0) != "236.321207":
                    continue

                target = element

    if target is None:
        logger.error("Target not found")
        return {"statusCode": 400, "status": "Error"}

    target_text = target.get_text()

    return_body = {"id": str(id)}
    if "Potential" in target_text:
        return_body["status"] = 1
    elif "No" in target_text:
        return_body["status"] = 0
    else:
        return_body["status"] = -1
    logger.info(return_body)

    table.put_item(Item=return_body)

    return {"statusCode": 200, "status": "success"}
