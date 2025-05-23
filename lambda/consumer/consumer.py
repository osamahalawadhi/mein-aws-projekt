import json
import boto3
import time

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('ProjektDatenOsamah')

def lambda_handler(event, context):
    for record in event['Records']:
        msg = json.loads(record['Sns']['Message'])

        if 'email' not in msg:
            print("❌ Fehlendes 'email' Attribut in Nachricht:", msg)
            continue

        item = {
            'id': str(int(time.time() * 1000)),
            **msg
        }

        print("✅ Nachricht empfangen und wird gespeichert:", item)

        table.put_item(Item=item)

    print("✅ Speicherung abgeschlossen.\n---")
    return {
        'statusCode': 200
    }
