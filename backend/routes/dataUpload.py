from fastapi import APIRouter
from ml import get_prediction

data_router = APIRouter(tags=["data-upload"])


from pydantic import BaseModel

class Data(BaseModel):
    data: str

@data_router.post("/upload", response_model=Data)
def process_data_upload(data: Data):
    res = get_prediction(data.data)
    return {"data": res}