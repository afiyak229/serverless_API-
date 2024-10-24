import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourDynamoDBTable')

def lambda_handler(event, context):
    operation = event['httpMethod']
    if operation == 'GET':
        return get_item(event)
    elif operation == 'POST':
        return put_item(event)
    elif operation == 'PUT':
        return update_item(event)
    elif operation == 'DELETE':
        return delete_item(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported operation')
        }

def get_item(event):
    key = json.loads(event['body'])['id']
    try:
        response = table.get_item(Key={'id': key})
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }

def put_item(event):
    item = json.loads(event['body'])
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Item created successfully')
        }
    except ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }

def update_item(event):
    # Update logic
    pass

def delete_item(event):
    # Delete logic
    pass

