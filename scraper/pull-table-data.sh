#!/bin/bash
set -eo pipefail
aws dynamodb scan --table-name archeo-results --region us-east-1 --output json > /archeo-data.json