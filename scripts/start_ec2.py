
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Target ONLY the "test" instance
    response = ec2.describe_instances(Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['test']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ])

    instance_ids = [instance['InstanceId']
                  for reservation in response['Reservations']
                  for instance in reservation['Instances']]

    if instance_ids:
        ec2.start_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f"Started instance: {instance_ids[0]} (test)"
        }
    return {
        'statusCode': 200,
        'body': "Instance 'test' not found or already running"
    }
