# from fastapi import APIRouter, Body, Request, Response, HTTPException, status
# from fastapi.encoders import jsonable_encoder
# from typing import List
# from Models.QueueModel import Queue
# from Services.queue_service import UserQueue
# from auth import AuthHandler
# router = APIRouter()


# @router.post('/register', status_code=201)
# def register(auth_details: AuthHandler):
#      if any(x['username'] == auth_details.username for x in users):
#          raise HTTPException(status_code=400, detail='Username is taken')
#      hashed_password = auth_handler.get_password_hash(auth_details.password)
#      users.append({
#        'username': auth_details.username,
#       'password': hashed_password
#      })
#      return

# @router.post('/login')
# def login(auth_details: AuthHandler):
#      user = None
#      for x in users:
#          if x['username'] == auth_details.username:
#              user = x
#              break

#      if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
#          raise HTTPException(status_code=401, detail='Invalid username and/or password')
#      token = auth_handler.encode_token(user['username'])
#      return {'token': token}


# @router.get('/unprotected')
# def unprotected():
#      return {'hello': 'world'}


# @router.get('/protected')
# def protected(username=Depends(auth_handler.auth_wrapper)):
#      return {'name': username}