from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from Utils import json_util
import threading
import asyncio


from Models.UserModel import User
from pika_client import Rabbit
from bot.abs_bot import Bot
from Services.consumer import Consumer

router = APIRouter()

@router.post("/start_live_transfer", response_description = "Create a new Queue", status_code = status.HTTP_201_CREATED)
def start_live_data(request: Request, user: User = Body(...)):
    
        user_json = jsonable_encoder(user)
        result = user_json
        pika_client = Rabbit()
        bot = Bot(pika_client, user.username, user.symbol)

        thread = threading.Thread(target=lambda: asyncio.run(Consumer.create_consumers()))
        thread.setName(user["username"] + "_" + "consumer_thread")
        thread.setDaemon(True)
        thread.start()  
       


        response = {
            "Status": status.HTTP_200_OK,
            "Message": f'{result} +has started to consume intervals',
            "Data": []
        }
        return response