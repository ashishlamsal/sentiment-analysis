from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

origins = ["*"]

from routes.dataUpload import data_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_router, prefix="/run")


if __name__ == "__main__":
    port = 8000
    while True:
        try:
            uvicorn.run("main:app", host="localhost", port=port, reload=True)
            break
        except:
            print("port ", port, " is occupied trying ", port + 1)
            port = port + 1
