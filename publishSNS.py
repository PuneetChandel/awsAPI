import boto3
import json

session = boto3.Session(profile_name='default')
sns = session.client('sns')

message= {"Brand" : "Audi",
          "Model":"Q5",
          "Year":"2018",
          "price":"50000",
          "currency":"USD"}

json_message = json.dumps(message)

try:
    response=sns.publish(
        TopicArn='arn:aws:sns:us-east-1:879458679876:pchandel-cloud',
        Message=json_message,
        Subject='Vehicle record'
        )

    print("Response from aws : ", response)
except Exception as e:
    print("Exception while publishing to SNA", e)
