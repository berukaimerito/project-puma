# AN AGGREGATION OF DATA THAT SHOULD BE SAVED INTO THE DATABASE

## Data aggregation is any process whereby data is gathered and expressed in a summary form. When data is aggregated, atomic data rows -- typically gathered from multiple sources -- are replaced with totals or summary statistics.



## BURAYA ACQUIRE DATA'DAN METODIZE, EVET METODIZE ETTIGIN TICKER TOPLAMA ISLEMLERINI



## Fili kucuk parcalara ayir
# microtask
# microtask (kata 7)



## FLASK ILE CELERY TASK ATADIGIN

## acquire_data.py 'dan importlanan methodu cagirarak save yapocaksin


from pymongo import MongoClient   ## pymongo burada ayni kapiya cikiyo  maksat bir tane python fileinda baglanmak
# from flask-mongoengine import mongoengine
from bson import ObjectId
import sys, os, inspect

# pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# sys.path.append(pathapp + "/config")
# import Environment as env
#
#
# class MongoDb(object):
#
#     def __init__(self):
#         self.moConn = MongoClient('mongodb://' + env.MONGO_HOST + ':' + env.MONGO_PORT)
#         self.dbname = self.moConn[env.MONGO_DB] ## app.py degerleri
#
#     def insert(self, collection, data):
#         newRowId = self.dbname[collection].insert(data) #istenilen dokumana istedigimizi kayddetme. yalniz buradaki soru
# database de olan tickerlari timeserioes olarak elealabilme
#         print
#         "New Row id: " + `newRowId`
#         self.moConn.close()
# a start.
# def initialize_db(app):
#     connect(host=app.config['MONGODB_SETTINGS'])

# Marcin'e gore bu tarz her yerde kullanilan connect'dir app vs dont repeat yourself diye util file kullanin demisti hazorlari bulunabilir


