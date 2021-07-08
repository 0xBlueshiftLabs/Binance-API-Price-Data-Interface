import requests
import json
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def get_binance_data(symbol, interval, startTime, endTime):

    # e.g. 'ETHUSDT','1h', dt.datetime(2020,1,1), dt.datetime(2020,2,1)

    # binance API url
    url = "https://api.binance.com/api/v3/klines"

    startTime = str(int(startTime.timestamp()*1000))
    endTime = str(int(endTime.timestamp()*1000))

    limit = 1000 # limit of bars (usually constrained by API call limit)

    req_params = {"symbol" : symbol, "interval" : interval, "startTime" : startTime,
                  "endTime" : endTime, "limit" : limit}

    df = pd.DataFrame(json.loads(requests.get(url, params = req_params).text))

    if (len(df.index) == 0):
        return None

    df = df.iloc[:, 0:6]
    df.columns = ['datetime','open','high','low','close','volume']

    df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.datetime]

    return df


months = [dt.datetime(2020, i, 1) for i in range(1,13)]
months.append(dt.datetime(2021,1,1))

df_list = [get_binance_data('ETHUSDT','1h',months[i], months[i+1]-dt.timedelta(0,1)) for i in range(0,(len(months)-1))]

df = pd.concat(df_list)
print(df.shape)

df['close'].astype('float').plot()
plt.show()
