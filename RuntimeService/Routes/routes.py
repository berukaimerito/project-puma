from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from Utils import json_util
import threading
import asyncio

from Models.UserModel import User

from Services.consumer import Consumer
from rabbit import Rabbit

router = APIRouter()
from supervisor import Supervisor
from bot import Bot


@router.post("/start_live_transfer", response_description="Create a new Queue", status_code=status.HTTP_201_CREATED)
def start_live_data(request: Request, user: User = Body(...)):
    conn = Rabbit()
    supervisor = Supervisor()
    bot = Bot(username=user.userName, symbol=user.symbol, app=conn)
    thread = threading.Thread(target=lambda: asyncio.run(supervisor.consume_intervals(bot)))
    thread.setName(bot.username + "_" + "consumer_thread")
    thread.setDaemon(True)
    thread.start()






    user_json = jsonable_encoder(user)
    result = user_json

    response = {
        "Status": status.HTTP_200_OK,
        # "Message": result,
        "Data": []
    }
    return response

# def start_threading(botlists):
#     for bot in botlists:
