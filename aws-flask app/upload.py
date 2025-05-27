from werkzeug.utils import secure_filename
import boto3
import os

bucket_name = 'my-tf-test-bucket-pranjal'

def upload_my_file(f):
    try:
        # Secure the filename and save to /tmp
        filename = secure_filename(f.filename)
        temp_path = os.path.join("/tmp", filename)
        f.save(temp_path)

        # Create S3 client
        s3client = boto3.client('s3')

        # Upload file to S3
        s3client.upload_file(temp_path, bucket_name, filename)

        print(f"File '{filename}' uploaded successfully.")
        return filename

    except Exception as e:
        print(f"Error during file upload: {e}")
        raise
