from uuid import uuid4

import boto3
from fastapi import UploadFile

from app.config import S3Config

__s3_client = boto3.client(
    's3',
    aws_access_key_id=S3Config.ACCESS_KEY,
    aws_secret_access_key=S3Config.SECRET_KEY
)


def upload_file_on_s3(file: UploadFile):
    random_file_name = uuid4().hex
    __s3_client.upload_fileobj(
        file.file,
        S3Config.BUCKET_NAME,
        random_file_name,
        ExtraArgs={'ContentType': 'image/jpeg'}
    )

    return {
        'image_path': f'https://{S3Config.BUCKET_NAME}.s3.{S3Config.LOCATION}.amazonaws.com/{random_file_name}'
    }
