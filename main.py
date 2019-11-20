import pandas as pd
import matplotlib.pyplot as plt 


def get_technical_indicators(dataset):
    # Create 7 and 21 days Moving Average
    dataset['ma7'] = dataset['Bid Price'].rolling(window=7).mean()
    dataset['ma21'] = dataset['Bid Price'].rolling(window=21).mean()
    """
    # Create MACD
    dataset['26ema'] = pd.ewm(dataset['Bid Price'], span=26).mean()
    dataset['12ema'] = pd.ewm(dataset['Bid Price'], span=12).mean()
    dataset['MACD'] = (dataset['12ema']-dataset['26ema'])"""

# Create Bollinger Bands)
    dataset["20sd"] = dataset['Bid Price'].rolling(window = 20).std()
    dataset['upper_band'] = dataset['ma21'] + (dataset['20sd']*2)
    dataset['lower_band'] = dataset['ma21'] - (dataset['20sd']*2)
    
    # Create Exponential moving average
    dataset['ema'] = dataset['Bid Price'].ewm(com=0.5).mean()
    
    # Create Momentum
    dataset['momentum'] = dataset['Bid Price']-1
    
    return dataset


file = "market_data.csv"


df = pd.read_csv(file,parse_dates=True)



esx = df.loc[df["Instrument"]=="ESX-FUTURE"]

sp  = df.loc[df["Instrument"]=="SP-FUTURE" ]


sp=sp.set_index("Timestamp")
sp_bp = sp["Bid Price"]
sp_ap = sp["Ask Price"]

df2= get_technical_indicators(sp).drop(["Instrument", "Ask Price" , "Ask Volume"],axis =1 )


df2.plot( )

