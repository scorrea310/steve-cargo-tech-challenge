import boto3
import datetime

this_is_a_shitty_variable_name_and_i_hate_when_other_people_do_this = "us-west-1"

seven_days_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
    days=7
)

ec2_client = boto3.client(
    "ec2",
    region_name=this_is_a_shitty_variable_name_and_i_hate_when_other_people_do_this,
)

response = ec2_client.describe_instances(
    Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
)

instances = []
for reservation in response["Reservations"]:
    instances.extend(reservation["Instances"])

for instance in instances:
    instance_id = instance["InstanceId"]
    ec2_launch_time = instance["LaunchTime"]

    print(f"Instance ID: {instance_id}")
    print(f"Launched {ec2_launch_time}")

    if ec2_launch_time < seven_days_ago:
        print("instance was created more than 7 days ago.")
        ec2_client.stop_instances(InstanceIds=[instance_id])
    else:
        print(ec2_launch_time, "ec2 is newer than 7 days")
