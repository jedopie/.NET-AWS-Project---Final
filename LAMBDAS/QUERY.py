import json
import boto3
import simplejson as json
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('music')
    body = table.scan()
    items = body['Items']
    
    
    event = json.loads(event['body'])
    items = json.loads(json.dumps(items))
    
    response = table.query(
        KeyConditionExpression=Key("title").eq("Lonesome Town") & Key("year").eq(1958))
    
    # res = table.get_item(Key={"year" : 1958, "title" : "Lonesome Town"
    # })
    # print(items[0]['title'])
    i =[]
    
    for item in items:
        # ONLY TITLE
        if (event['artist'] == "" and event['year'] == "" and event['title'] == item['title']):
            i.append(item)
        # ONLY ARTIST
        elif (event['title'] == "" and event['year'] == "" and event['artist'] == item['artist']):
            i.append(item)
        # ONLY YEAR
        elif (event['artist'] == "" and event['title'] == "" and event['year'] == str(item['year'])):
            i.append(item)
        # TITLE AND YEAR
        elif (event['artist'] == "" and event['title'] == item['title'] and event['year'] == str(item['year'])):
            i.append(item)
        # TITLE AND ARTIST
        elif (event['year'] == "" and event['title'] == item['title'] and event['artist'] == item['artist']):
            i.append(item)
        # YEAR AND ARTIST
        elif (event['title'] == "" and event['artist'] == item['artist'] and event['year'] == str(item['year'])):
            i.append(item)
        # ALL
        elif (event['title'] == item['title'] and event['artist'] == item['artist'] and event['year'] == str(item['year'])):
            i.append(item)


            

    if (len(i) > 0):
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'statusCode': 200,
            'body': json.dumps(i)
        }
    else:
        return {
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'statusCode': 409,
            # 'body': json.dumps(i)
        }
        
