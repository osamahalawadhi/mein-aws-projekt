import json
import boto3
import time

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:eu-west-1:788174142154:MeinProjektTopicOsamah'

def producer(event, context):
    body_str = event.get('body')
    if not body_str:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No body found in request'})
        }
    body = json.loads(body_str)

    name = body.get('name', 'Unbekannt')
    feedback = body.get('feedback', 'Kein Feedback')

    message = {
        'name': name,
        'feedback': feedback,
        'email': 'testuser@example.com'
    }

    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Message=json.dumps(message)
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Feedback erfolgreich gesendet'})
    }
