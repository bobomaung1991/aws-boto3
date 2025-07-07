
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    return {
        'statusCode': 200,
        'body': [bucket['Name'] for bucket in buckets['Buckets']]
    }
