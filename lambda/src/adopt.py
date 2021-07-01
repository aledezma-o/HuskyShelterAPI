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

def handler(event, context):
    print(json.dumps({'runnin': True}))
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda')
    } 
    
def solicitAdoption(event, context):
    print(json.dumps({'runnin': True}))
    print(json.dumps(event))
    
    path = event["path"]
    array_path = path.split("/")
    user_id = array_path[-1]
    table.
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda')
    } 