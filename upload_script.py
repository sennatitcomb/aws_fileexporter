import os 
import glob
os.system('python3 -m pip install boto3')

import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


def upload_files(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

path = './traces/*.json'
files = glob.glob(path)
for i in files:
    s3_file = f"topics/trace_topics/{os.path.basename(i)}" 
    uploaded = upload_files(i, 'bucket', s3_file)
    
path = './metrics/*.json'
files = glob.glob(path)
for i in files:
    s3_file = f"topics/metric_topics/{os.path.basename(i)}" 
    uploaded = upload_files(i, 'bucket', s3_file)
