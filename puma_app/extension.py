from flask import (
    Flask,
    render_template, 
    Blueprint,
    jsonify,
    request,
    redirect, 
    session,
    flash
 )
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin
import string
import secrets

alphabet = string.ascii_letters + string.digits
secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
csrf = CSRFProtect()