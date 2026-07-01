from fastapi import FastAPI
from contextlib import asynccontextmanager



models={}
@asynccontextmanager
async def lifespan(app:FastAPI):
    #loading the models
    models["class names"]=joblib.load("models/class_names.json")
    yield
    models.clear()

app = FastAPI(lifespan=lifespan,
              title="Spam detection API",
              version="1.0",
              description="Detecting spam messages using SVC And TfidfVectorizer")