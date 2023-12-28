from binance import Client
from binance.enums import HistoricalKlinesType
from datetime import datetime,timedelta

client=Client("GUf7tyd95mZMW7xXhKSuXXUhvenGaFZURNrrYFmecqZfFKGuzmYO9dRoPPR1xHTh","FGTiA20a37iEQzTgpv8pQnI4QIeNVlx6EEq5Dfu5rHB60tZVHNB1US8bc4Zu4atw")


# # Replace 'your_api_key' and 'your_api_secret' with your actual Binance API key and secret


def get_one_year_data(symbol):
    # Calculate the start date (1 year ago from now)
    start_date = datetime.now() - timedelta(days=1050)

    # Convert start_date to milliseconds
    start_date_ms = int(start_date.timestamp()) * 1000

    # Get klines data for the symbol and interval '1d' (1 day)
    klines = client.get_klines(symbol=symbol, interval='1d', startTime=start_date_ms)

    return klines

# Replace 'BTCUSDT' with the symbol you are interested in
symbol_data = get_one_year_data('IOTAETH')
print(symbol_data)


# Iterate over each kline entry and print it
# for kline in symbol_data:
#     print("Open time:", datetime.utcfromtimestamp(kline[0] / 1000).strftime('%Y-%m-%d %H:%M:%S'))
#     print("Open:", kline[1])
#     print("High:", kline[2])
#     print("Low:", kline[3])
#     print("Close:", kline[4])
#     print("Volume:", kline[5])
#     print("Close time:", datetime.utcfromtimestamp(kline[6] / 1000).strftime('%Y-%m-%d %H:%M:%S'))
#     print("-------")


# # # klines = client.get_historical_klines("BTCUSDT", '5m',limit=2,klines_type=HistoricalKlinesType.FUTURES)
# # data=client.get_all_tickers()
# # symbols=[]

# # for symbol in data:
# #     symbols.append(symbol['symbol'])
# # print((symbols))


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://sudhanshus883:uWZLgUV61vMuWp8n@cluster0.sxyyewj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
bot=client['bot']
admin=bot['admin']
data=bot['data']

admin_data=admin.find_one()
symbols=admin_data['symbols']
api_key=admin_data['api_key']
secret_key=admin_data['secret_key']
# client=login(api_key,secret_key)

# print(data.find_one())
# data.delete_many({})
# # # data.insert_one({"BTCUSDT":0})
# # # for symbol in symbols:
# # #     if data.find_one({str(symbol):{"$exists":True}}):
# # #         print("DOES")
# # #     else:
# # #         print("DOESN'T")

# from datetime import datetime

# print(datetime.now().minute)
