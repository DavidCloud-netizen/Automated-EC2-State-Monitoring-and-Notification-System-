import boto3
import os

def lambda_handler(event, context):
    # Initialize clients for EC2, S3, and SES
    ec2_client = boto3.client("ec2")
    s3_client = boto3.client("s3")
    ses_client = boto3.client("ses")

    # Fetch the state of all EC2 instances
    ec2_response = ec2_client.describe_instances()
    instance_states = []

    for reservation in ec2_response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_states.append(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

    # Fetch the list of S3 buckets and their contents
    s3_buckets = s3_client.list_buckets()["Buckets"]
    s3_content_list = []
    
    for bucket in s3_buckets:
        bucket_name = bucket["Name"]
        s3_content_list.append("\nContents of bucket: " + bucket_name)
        try:
            objects = s3_client.list_objects_v2(Bucket=bucket_name)
            if "Contents" in objects:
                for obj in objects["Contents"]:
                    s3_content_list.append(f"  - {obj['Key']} (Size: {obj['Size']} bytes, LastModified: {obj['LastModified']})")
            else:
                s3_content_list.append("  - No objects found.")
        except Exception as e:
            s3_content_list.append(f"  - Error accessing bucket: {str(e)}")

    # Create email content
    email_content = "EC2 Instance States:\n" + "\n".join(instance_states)
    email_content += "\n\nS3 Buckets and Contents:\n" + "\n".join(s3_content_list)

    # Send email using SES
    try:
        ses_client.send_email(
            Source=os.environ["EMAIL_SOURCE"],
            Destination={"ToAddresses": [os.environ["EMAIL_DESTINATION"]]},
            Message={
                "Subject": {"Data": "AWS Resources State"},
                "Body": {"Text": {"Data": email_content}},
            }
        )
        return {"statusCode": 200, "body": "Email sent successfully!"}
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to send email: {str(e)}"}