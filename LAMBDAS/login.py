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
        r = json.dumps(response["Items"][0])
        x = json.loads(r)
        
        password = x['password']
        
    
        if ((response['Items'] and password == event['password'])):
            return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response['Items'][0])
        }
        else:
            return {
            'statusCode': 404,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            # 'body': 
        }
    else:
        return {
        'statusCode': 404,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        # 'body': event['body']
    }

