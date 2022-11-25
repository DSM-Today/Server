from fastapi import APIRouter, UploadFile

from app.core.image.service import upload_file_on_s3

image_router = APIRouter()


@image_router.post('/images')                          # 인가가 필요할까? TODO
def upload_file(file: UploadFile):
    return upload_file_on_s3(file)