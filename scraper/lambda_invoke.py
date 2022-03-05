import json
import random
import time

import boto3


def main():

    lambda_client = boto3.client("lambda")

    with open("./ids.geojson") as f:
        data = json.load(f)

    result = []
    for feature in data["features"]:
        id = feature["properties"]["ASMT"]
        result.append({"id": id})


    for idx, row in enumerate(result):
        payload = {
            "id": row["id"]
        }

        _ = lambda_client.invoke(
            FunctionName='napa',
            Payload=json.dumps(payload),
            InvocationType='Event'
        )
        time.sleep(random.randrange(18, 20, 1) / 10)

        if idx % 300 == 0:
            print(idx, " dispatched ", row["id"])
            time.sleep(random.randrange(200, 210, 1) / 10)
        elif idx % 100 == 0:
            print(idx, " dispatched ", row["id"])
            time.sleep(random.randrange(100, 105, 1) / 10)
        elif idx % 10 == 0:
            print(idx, " dispatched ", row["id"])
            time.sleep(random.randrange(30, 35) / 10)


if __name__ == "__main__":
    print("Starting...")
    main()
    print("Done!")
