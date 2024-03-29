from Services.event_loop_service import work as StartDbLoop
from Services.event_loop_service import feed_queue as StartQueueLoop
from fastapi import FastAPI, Request
from dotenv import dotenv_values
from pymongo import MongoClient
from Routes.queue_routes import router as queue_router
import asyncio
import threading

config = dotenv_values()

app = FastAPI()
app.include_router(queue_router, tags=["Queue Operations"])


@app.on_event("startup")
async def startup_event():
    app.mongodb_client = MongoClient(config["MongoDB_Uri"])
    app.database = app.mongodb_client[config["DB_Name"]]

    try:
        app.database.create_collection(config["Collection_CandleStick"])
        app.database.create_collection(config["Collection_Ticker"])
        app.database.create_collection(config["Collection_User"])
    except:
        pass

    thread_db = threading.Thread(target=lambda: asyncio.run(StartDbLoop(app)))
    thread_db.setName("thread_db")
    thread_db.start()
    thread_queue = threading.Thread(target=lambda: asyncio.run(StartQueueLoop(app)))
    thread_queue.setName("thread_queue")
    thread_queue.start()


@app.on_event("shutdown")
async def shutdown_event():
    app.mongodb_client.close()


@app.get("/sum")
async def sum_numbers():
    numbers = 'annesi'
    return {"sum": (numbers)}


import uvicorn


# uvicorn.run(app, host="0.0.0.0", port=8000)
