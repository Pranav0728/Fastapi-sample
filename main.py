from fastapi import FastAPI, HTTPException
from routes import router 

app = FastAPI()
app.include_router(router)
