from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
from Models.UserModel import User
from pika_client import Rabbit
from bot.abs_bot import Bot
from consume import supervisor

router = APIRouter()

@router.post("/start_live_transfer", response_description = "Create a new Queue", status_code = status.HTTP_201_CREATED)
def start_live_data(request: Request, user: User = Body(...)):
    
        user_json = jsonable_encoder(user)
        result = user_json
        pika_client = Rabbit()
        bot = Bot(pika_client, user.username, user.symbol)
        supervisor(bot)