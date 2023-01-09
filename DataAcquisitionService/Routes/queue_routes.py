import time
from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from models.QueueModel import Queue
from Services.queue_service import UserQueue
global users
import requests
import json

user_list = []
router = APIRouter()

@router.post("/create_queue", response_description="Create a new Queue",
             status_code=status.HTTP_201_CREATED)  # response_model = Queue
def create_queue(request: Request, queue: Queue = Body(...)):
    
    user_queue = UserQueue(queue.userName, queue.symbol)
    user_list.append(user_queue)
    time.sleep(2)
    queue_json = jsonable_encoder(queue)
    result = user_queue.start_feeding(user_queue)


    json_object = json.dumps(   {
            'userName': queue.userName,
            'symbol':queue.symbol
        })
        
    loaded_r = json.loads(json_object)
    requests.post('http://127.0.0.1:8086/start_live_transfer',json=loaded_r)
    print("Request sent to RunTime")

    response = {
        "Status": status.HTTP_200_OK,
        "Message": result,
        "Data": queue_json
    }
    return response


@router.post("/stop_queue", response_description="Stop an existing Queue",
             status_code=status.HTTP_201_CREATED)  # response_model = Queue
def stop_queue(request: Request, queue: Queue = Body(...)):


    for user_queue in user_list:
        if user_queue.user_name == queue.userName and user_queue.symbol == queue.symbol:
            print("31")
        #DB connection'A SAHIBIZ