from fastapi import FastAPI
import uvicorn


from routes.dataUpload import data_router

app = FastAPI()
app.include_router(data_router,prefix='/data')


if __name__ == "__main__":
    port = 8000
    while True:
        try:
            uvicorn.run("main:app", host="localhost", port=port, reload=True)
            break
        except:
            print("port ", port, " is occupied trying ", port+1)
            port = port+1
