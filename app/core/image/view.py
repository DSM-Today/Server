from fastapi import APIRouter, UploadFile

from app.core.image.service import upload_file_on_s3

image_router = APIRouter(
    prefix='/images'
)


@image_router.post('')
def upload_file(file: UploadFile):
    return upload_file_on_s3(file)