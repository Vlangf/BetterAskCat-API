from fastapi import FastAPI
from api.batteraskcat_api import router as batteraskcat_router

app = FastAPI()

# Include the API router
app.include_router(batteraskcat_router)
