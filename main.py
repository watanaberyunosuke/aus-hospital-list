from fastapi import FastAPI
from database import Base, engine

import hospital
import route

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=route.router)

@app.get("/")
async def root():
    return {"message": "fastapi"}
