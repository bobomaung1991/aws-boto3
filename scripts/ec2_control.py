
import boto3

ec2 = boto3.client('ec2')

def stop_instance(i-03ea70aa92200555c):
    ec2.stop_instances(InstanceIds=[i-03ea70aa92200555c])
    print(f"Stopped instance: {i-03ea70aa92200555c}")

# Example: Stop an EC2 instance
stop_instance('i-03ea70aa92200555c')  # ← Replace with your instance ID
~
~

