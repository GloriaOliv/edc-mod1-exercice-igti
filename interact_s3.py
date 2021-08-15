
import boto3
import pandas as pd


# Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

s3_client.upload_file("raw-data/MICRODADOS_ENEM_2019.csv",
                      "datalake-gloria-556116348126",
					  "raw-data/MICRODADOS_ENEM_2019.csv")