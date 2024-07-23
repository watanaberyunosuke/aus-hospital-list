import os
from fastapi import FastAPI
from database import Base, engine

import route

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=route.router)


@app.get("/")
async def root():
    return "For API go to: https://aus-hospital-list.vercel.app/api/v1/hospitals"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
