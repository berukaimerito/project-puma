import time
from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
import threading
import asyncio
from models.user_model import User
from rabbit import Rabbit
from dotenv import dotenv_values
from bot import Bot
from supervisor import Supervisor
import os
import importlib.machinery

config = dotenv_values()
router = APIRouter()

import importlib


@router.post(
    "/start_live_transfer",
    response_description="Create a new Queue",
    status_code=status.HTTP_201_CREATED,
)
def start_live_data(request: Request, user: User = Body(...)):
    conn = Rabbit()
    supervisor = Supervisor()

    # Get the current working directory
    cwd = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
    file_path = os.path.join(parent_dir, "api/user_scripts", f"{user.username}{user.symbol}.py")

    module = importlib.machinery.SourceFileLoader("module", file_path).load_module()
    bot = module.Bot(username=user.user_name, symbol=user.symbol, app=conn)

    print(type(bot))

    supervisor.supervisor_bot_list.append(bot)
    time.sleep(5)

    thread = threading.Thread(
        target=lambda: asyncio.run(supervisor.consume_intervals(bot))
    )
    thread.setName(f"{user.userName}_consumer_thread")
    thread.setDaemon(True)
    thread.start()

    user_json = jsonable_encoder(user)
    result = user_json

    response = {
        "status": status.HTTP_200_OK,
        "data": [],
    }
    return response