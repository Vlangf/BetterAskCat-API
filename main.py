from fastapi import FastAPI
from api.batteraskcat_api import router as batteraskcat_router

app = FastAPI(docs_url=None, redoc_url=None)

# Include the API router
app.include_router(batteraskcat_router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8002)