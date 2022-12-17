from fastapi import FastAPI
from dotenv import dotenv_values
from Routes.routes import router
from bot import Bot
from rabbit import Rabbit
config = dotenv_values()
from supervisor import Supervisor
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("Application Starting...")
    supervisor = Supervisor()

    pass

@app.on_event("shutdown")
async def shutdown_event():
    print("Application Closing...")
    pass

app.include_router(router, tags=["Live Data Consume"])
