from fastapi import FastAPI
import uvicorn

from core.application.endpoints import rout

app = FastAPI()
app.include_router(rout)