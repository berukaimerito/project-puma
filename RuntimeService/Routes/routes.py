import time

from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
import threading
import asyncio
from Models.UserModel import User
from rabbit import Rabbit

from bot import Bot
from supervisor import Supervisor


router = APIRouter()


@router.post("/start_live_transfer", response_description="Create a new Queue", status_code=status.HTTP_201_CREATED)
def start_live_data(request: Request, user: User = Body(...)):

    conn = Rabbit()
    supervisor = Supervisor()

    #########BO
    bot = Bot(username=user.userName, symbol=user.symbol, app=conn)
    supervisor.supervisor_bot_list.append(bot)
    time.sleep(5)
    # if bot:
    thread = threading.Thread(target=lambda: asyncio.run(supervisor.consume_intervals(bot)))
    thread.setName(user.userName + "_" + "consumer_thread")
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
