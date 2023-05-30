from fastapi import FastAPI
import uvicorn
from resources.routes import api_router

app = FastAPI()
app.include_router(api_router)#yo


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
