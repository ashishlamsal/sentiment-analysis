from fastapi import APIRouter
from ml import get_prediction

data_router = APIRouter(tags=["run-predict"])


from pydantic import BaseModel


class Data(BaseModel):
    data: str


@data_router.post("/predict")
def process_data_upload(data: Data):
    res = get_prediction(data.data)
    return {"data": res}
