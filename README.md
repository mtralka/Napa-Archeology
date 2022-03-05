# Napa County, CA Public Parcel Archeology

[Website](https://napa-archeology.netlify.app/)

*S3 bucket with all parcel pdfs available upon request*

## Problem

Napa County, CA identifies public land parcels with potential archeology sites. While this data is *technically* open-source, the information is obfuscated across several data products making it **obtusely difficult** for citizens to locate potential sites for amateur archeological exploration.

Normally, end-users would have to download the public land parcel information [here](https://gis.napa.ca.gov/giscatalog/catalog_xml.asp?srch_opt=all&db_name=x&theme=x&sort_order=layer&meta_style=fgdc&submit=Submit) ([metadata found here](https://gis.napa.ca.gov/giscatalog/viewXML.asp?Name=MAINGIS.GIS.PARCELS_PUBLIC&meta_style=fgdc) and then query each respective public parcel by ASMT (id) code [here](https://www.countyofnapa.org/1935/Parcel-Data-Report). After querying, the interface returns a ~3mb PDF parcel data report which in-part contains information about potential archeology sites. This process is not conducive for efficient field exploration.

## Solution

Leveraging AWS lambda, dynamo db, and S3, I created a serverless pipeline to generate a data product containing the potential archeological status of each public parcel in Napa County. The lambda function calls the Napa County PDF Query Builder API endpoint, retrieves the parcel report pdf, scrapes the pdf to determine if archeological sites are present, and then saves the pdf to S3 and the archeological information to dynamo db.

Following data aquisition, I created a Vue 3 frontend (Vite, WindiCSS, Netlify) to display the aquired information using DeckGL and Mapbox GL. The frontend features user selectable baselayers, per-parcel popups for ASMT IDs, and geolocation services to provide in-the-field reference points.

The overall solution steps are outlined below. Aside from the time required to scrape the report PDFs, this project took under a day from real-world problem identification to finalized product.

## Solution Steps

- Identifed specific API endpoint for parcel report generator
  - `https://gis.napa.ca.gov/SQLReportGen/Report.ashx?ReportPath=/GIS%20Reports/Parcel_Summary_Report&opts=ASMT|${ASMT_ID}`
  - tested endpoint for rate limitations, error codes, response time
  - used `requests` python package
- Identified format of returned PDF to determine x,y coordinates of desired archeological information
  - used `PDFMiner.six` python package
  - archeology information can be one of 2 texts:
    - `Potential Archeological sites may occur in the general area`
    - `No archeological sites found`
- Built serverless AWS lambda function to invoke API call, parse returned PDF, and store results in NoSQL Dynamo DB databse and PDF in S3
  - code in `./scraper/*`
  - generate required dependency layer using `build-layer.sh`
- Generated all possible ASMT IDs using public land parcel shapefile metadata and QGIS
  - `./scraper/ids.geojson`
- Built `./scraper/lambda_invoke.py` to invoke lambda function asynchronously within the rate limitations imposed by endpoint
  - using `boto3`
  - runtime roughly 36 hours for ~50k parcels
- Pull Dynamo DB data with `./scraper/pull-table-data.sh`
- Converted DynamoDB formatted `/archeo-data.json` to usable JSON  with `./scraper/clean_table_data.py`
- Built Vue 3 frontend
- :rocket: Deployed to Netlify
