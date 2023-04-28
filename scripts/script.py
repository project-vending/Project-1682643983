python
# Import necessary libraries
import boto3
from datetime import datetime
import time

# Set up AWS credentials and connect to Kinesis
aws_access_key_id = 'your_aws_access_key_id'
aws_secret_access_key = 'your_aws_secret_access_key'
kinesis = boto3.client('kinesis', region_name='us-west-2',
                       aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key)

# Define the Kinesis stream name
stream_name = 'kinesis-stream'

# Define the data ingestion function
def ingest_data(data):
    try:
        put_response = kinesis.put_records(StreamName=stream_name,
                                           Records=[
                                               {
                                                   'Data': data,
                                                   'PartitionKey': str(time.time())}
                                           ])
        print(put_response)
    except Exception as e:
        print(e)

# Define the main function
def main():
    while True:
        # Replace this with your own data ingestion logic
        data = f"Data at {datetime.now()}"
        ingest_data(data)
        time.sleep(1)

# Call the main function
if __name__ == "__main__":
    main()
