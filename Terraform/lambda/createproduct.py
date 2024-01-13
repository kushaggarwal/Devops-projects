import logging
import boto3
import json
import os


session = boto3.Session(region_name=os.environ['REGION'])
dynamodb_client = session.client('dynamodb')


def lambda_handler(event, context):
    try:
        print("event->" + str(event))
        payload = json.loads(event['body'])
        dynamodb_response = dynamodb_client.put_item(
            TableName = os.environ["PRODUCT_TABLE"],
            Item = {
                "product_id" : {
                    "S": payload["productId"]
                },
                "category" : {
                    "S": payload["category"]
                },
                "product_rating" : {
                    "S": payload["productRating"]
                },
                "product_name" : {
                    "S": payload["productName"]
                },
                "product_price" : {
                    "S": payload["productPrice"]
                },
                "product_description" : {
                    "S": payload["productDescription"]
                },
            }
        )
        print(dynamodb_response)
        return {
            'status_code' : 201,
            'body' : '{"status":"Product Created"}'
        }
    except Exception as e:
        logging.error(e)
        return {
            'status_code' : 500,
            'body' : '{"status":"Server Error"}'
        }
