

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from binance import Client
# Create your views here.

import json
import threading
import traceback
from datetime import datetime

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sudhanshus883:uWZLgUV61vMuWp8n@cluster0.sxyyewj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
bot=client['bot']
admin=bot['admin']
data=bot['data']

import logging
logger = logging.getLogger('dev_log')
errors=[]
logins={}


def login(api_key,secret_key):
    if api_key in logins:
        return logins[api_key]
    client=Client(api_key,secret_key)
    logins[api_key]=client
    return client


def main():
    try:

        minutes=int(datetime.now().minute)
        minutes=int((minutes+5)/5)*5
        # logger.info(str(minutes))
        if(minutes==60):
            minutes=0

        admin_data=admin.find_one()
        symbols=admin_data['symbols']
        api_key=admin_data['api_key']
        
        secret_key=admin_data['secret_key']

        client=login(api_key,secret_key)

        for symbol in symbols:
            
            if data.find_one({symbol:{"$exists":True}}):
                downloaded_data=client.get_klines(symbol=symbol,interval="5m",limit=1000)
                filter_criteria={symbol:{"$exists":True}}

                saved_data=data.find_one(filter_criteria)[symbol]
                last_time_stamp=saved_data[-1][0]
                # print(last_time_stamp)
                # saved_data.append(downloaded_data[0])
                index=0
                for candle in downloaded_data:
                    if(candle[0]==last_time_stamp):
                        break
                    index+=1
                for i in range(index+1,len(downloaded_data)-1):
                    saved_data.append(downloaded_data[i])


                update_data={"$set":{symbol:saved_data}}
                data.update_one(filter_criteria,update_data)
            else:
                symbol_data=client.get_klines(symbol=symbol,interval="5m",limit=1000)
                symbol_data.pop()
                data.insert_one({symbol:symbol_data})

        # while True:
        #     if(datetime.now().minute==minutes):
        #         break

    except Exception:
        if str(traceback.format_exc()) not in errors:
            logger.info(str(traceback.format_exc()))
            errors.append(str(traceback.format_exc()))

def loop():
    while True:
        main()


T=threading.Thread(target=loop)
T.start()

def extract(request,symbol):
    try:

        data1=data.find_one({symbol:{"$exists":True}})[symbol]
        
        list_of_dicts = [
            {
                'timestamp': sublist[0],
                'open': sublist[1],
                'high': sublist[2],
                'low': sublist[3],
                'close': sublist[4],
                'volume': sublist[5]
            }
            for sublist in data1
        ]

        # Convert the list of dictionaries to JSON
        json_data = json.dumps(list_of_dicts, indent=2)
        return JsonResponse(list_of_dicts,safe=False)

    except Exception:
        if str(traceback.format_exc()) not in errors:
            logger.info(str(traceback.format_exc()))
            errors.append(str(traceback.format_exc()))
        
        return JsonResponse({"error":str(traceback.format_exc())})
    

if __name__=="__main__":
    main()