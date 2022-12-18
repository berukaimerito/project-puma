from fastapi import FastAPI
from dotenv import dotenv_values
from Routes.routes import router
config = dotenv_values()
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("Application Starting...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Application Closing...")
    pass

app.include_router(router, tags=["Live Data Consume"])
