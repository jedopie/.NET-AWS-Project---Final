import json
import base64
import boto3
import simplejson as json
s3 = boto3.client('s3')

def lambda_handler(event, context):
    event = json.loads(event['body'])

    response = s3.get_object(Bucket="s3868658-images",
                         Key=event['title'])
     
    image = response['Body'].read()    
    print(image)
    b = base64.b64encode(image).decode("utf-8")
    # print(response)
    
    # print(response_json)
    # message = response_json['body']['message']
    # print(message)
    return {
        'headers': { 
            "Content-Type": "image/png", 
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'statusCode': 200,
        'body': b,
        'isBase64Encoded': True
        # 'body': json.dumps(response)
    }
