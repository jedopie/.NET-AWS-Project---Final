import json
import boto3
import simplejson as json
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    
    table = dynamodb.Table('login')
    body = table.scan()
    items = body['Items']
    event = json.loads(event['body'])
    
    response = table.query(KeyConditionExpression=Key('email').eq(event['email']))
    if (response['Items']):
        return {
        'statusCode': 409,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        # 'body': json.dumps(response['Items'])
    }
    
    else:
        table.put_item(Item={
        'email': event['email'],
        'password': event['password'],
        'user_name': event['user_name'],
    })
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(event)
        }