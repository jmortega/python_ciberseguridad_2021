import boto3
aws_access_key_id = ''
aws_secret_access_key = ''
region_name = 'ap-southeast-2'
session = boto3.session.Session(aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=region_name)
ec2client = session.client('ec2')
client_instance = ec2client.run_instances(
    ImageId='ami-30041c53',
    KeyName='Keys',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
