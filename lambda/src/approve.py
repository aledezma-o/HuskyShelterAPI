import json
import boto3
import base64
import os
import uuid

animal_adoption_table= os.environ['HUSKY_SHELTERS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(animal_adoption_table)
s3 = boto3.client('s3')
bucketName = 'bucket-pets'
sns = boto3.resource('sns') 

def handler(event, context):
    print(json.dumps({'runnin': True}))
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda')
    }

def solicitAdoption():
    print(json.dumps({'runnin': True}))