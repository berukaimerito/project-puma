import time
import os
import importlib.machinery
import importlib
from rabbit import RabbitCon
import threading
import asyncio
from models.queue_model import QueueModel
from supervisor import Supervisor
from fastapi import APIRouter, Body, Request, status
from dotenv import dotenv_values


config = dotenv_values()
router = APIRouter()




@router.post(
    "/start_live_transfer",
    response_description="Create a new Queue",
    status_code=status.HTTP_201_CREATED,
)
def start_live_data(request: Request, user: QueueModel = Body(...)):
    
    conn = RabbitCon()
    supervisor = Supervisor()

    # Get the current working directory
    cwd = os.getcwd()
    parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
    file_path = os.path.join(parent_dir, "api/user_scripts", f"{user.user_name}_{user.symbol}.py")

    module = importlib.machinery.SourceFileLoader("module", file_path).load_module()
    bot = module.Bot(username=user.user_name, symbol=user.symbol, app=conn)

    print(type(bot))

    supervisor.supervisor_bot_list.append(bot)

    time.sleep(5)

    thread = threading.Thread(
        target=lambda: asyncio.run(supervisor.consume_intervals(bot))
    )
    thread.setName(f"{user.user_name}_consumer_thread")
    thread.setDaemon(True)
    thread.start()

    response = {
        "status": status.HTTP_200_OK,
        "data": [],
    }
    return response