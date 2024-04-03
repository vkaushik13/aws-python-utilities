import pandas as pd
import boto3

def list_ec2_instances_with_tags(region_name):
    # Create an EC2 client
    ec2_client = boto3.client('ec2', region_name=region_name)

    # Describe all EC2 instances
    response = ec2_client.describe_instances()

    # Extract instance details and tags
    instance_details = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_tags = instance.get('Tags', [])
            instance_tags_dict = {tag['Key']: tag['Value'] for tag in instance_tags}
            instance_details.append({'Instance ID': instance_id,
                                     **instance_tags_dict})  # Merge tags into the dictionary

    return instance_details

def main():
    # AWS region
    aws_region = 'ap-southeast-2'  # Update with your desired AWS region

    # List EC2 instances and their tags
    instances = list_ec2_instances_with_tags(aws_region)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(instances)

    # Write DataFrame to Excel
    excel_filename = 'ec2_instance_details.xlsx'
    df.to_excel(excel_filename, index=False)

    print(f"EC2 instance details have been exported to '{excel_filename}'.")

if __name__ == "__main__":
    main()
