import pandas as pd
import requests
import boto3
import logging


# Create a function to make a request to a URL and get the text from the page
def get_text(url):
    response = requests.get(url)
    return response.text

sources = "data/sources.csv"
page_content = "data/page_content.csv"

# Load the sources datset
sources_df = pd.read_csv(sources)

# Load the pagecontent dataset
page_content_df = pd.read_csv(page_content)

# Combine the CSVs into one CSV
combined_df = pd.concat([sources_df, page_content_df], axis=1)

# Save the df
combined_df.to_csv("combined.csv", index=False)

# Function to upload a file to s3
def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True


# Test Your Url function
text = get_text(combined_df["source"][0])
print(text)
# Upload the file to combined CSV to S3

bucket = "YOUR_BUCKET"
upload_file_to_s3("combined.csv", bucket, "combined.csv")
