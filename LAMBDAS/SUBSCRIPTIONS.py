import json
import boto3
import simplejson as json
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('subscribe')
    music_table = dynamodb.Table('music')
    music_body = music_table.scan()
    music_items = music_body['Items']
    body = table.scan()
    items = body['Items']
    
    # if (event)
    event = json.loads(event['body'])
    
    music_items = json.loads(json.dumps(music_items))

    
    response = table.query(KeyConditionExpression=Key('email').eq(event['email']))
    if (response['Items']):
        if (response['Items']):
            r = json.dumps(response["Items"])
            x = json.loads(r)
            
        print(r)
        a = []
    
        for sub in x:
            # a.append(sub["song_title"])
            for song in music_items:
                if (sub['song_title'] == song['title']):
                    a.append(song)
            
        
        return {
            'headers': { 
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
            'statusCode': 200,
            'body': json.dumps(a)
        }
    else:
        return {
            'headers': { 
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
            'statusCode': 404,
        }
