from fastapi import FastAPI

from routes.doc import router

app = FastAPI()
app.include_router(router)