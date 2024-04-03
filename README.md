# AWS Tagging Scripts

This repository contains Python scripts for working with AWS resources, specifically for managing EC2 instance tags.

## Prerequisites

Before running the scripts, ensure you have the following prerequisites installed and configured:

- Python 3.x
- AWS CLI
- AWS profiles configured with appropriate permissions
- `awsume` installed and configured for assuming AWS roles

### Installing `awsume`

To install `awsume`, you can follow the instructions provided in the [official documentation](https://awsu.me/docs/installation.html).

Once installed, make sure to configure `awsume` with your AWS profiles using the `awsume --configure` command.

## Scripts

### `01_list_ec2_instances_with_tags.py`

This script lists EC2 instances in AWS and exports their details to Excel files.

#### Features

- Utilizes AWS SDK (boto3) to list EC2 instances.
- Exports instance details to Excel files.

#### Usage

1. Update the AWS region (`aws_region`) in the script if needed.
2. Run the script.

### `02_consolidate_ec2_excel_files.py`

This script consolidates multiple Excel files into one, with each profile's data organized in a separate tab.

#### Features

- Reads Excel files from a specified folder.
- Consolidates data from all Excel files into one DataFrame.
- Writes the consolidated data to a new Excel file.

#### Usage

1. Place all Excel files you want to consolidate into a folder.
2. Update the `folder_path` variable in the script to point to the folder containing your Excel files.
3. Run the script.

### `03_tagging_test_script.py`

This script is a test script for applying tags to EC2 instances.

#### Features

- Reads data from an Excel sheet containing server tags.
- Prints out the tags that would be applied to EC2 instances.

#### Usage

1. Ensure you have an Excel sheet named `servers_and_tags.xlsx` containing the server tags.
2. Update the AWS region (`aws_region`) in the script if needed.
3. Run the script.

## Requirements

The project dependencies are listed in the `requirements.txt` file.

To install the dependencies, run:

