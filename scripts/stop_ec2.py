
import boto3

sns = boto3.client('sns')

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
            'Values': ['running']
        }
    ])

    instance_ids = [instance['InstanceId']
                  for reservation in response['Reservations']
                  for instance in reservation['Instances']]

    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        return {
            'statusCode': 200,
            'body': f"Stopped instance: {instance_ids[0]} (test)"
        }
    return {
        'statusCode': 200,
        'body': "Instance 'test' not found or already stopped"
    }


    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:851725574271:EC2StopAlerts',
            Message=f"Stopped EC2 instance: test ({instance_ids[0]}) at {datetime.datetime.now()}"
        )
