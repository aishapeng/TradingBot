from sklearn.preprocessing import MinMaxScaler
from indicators import *

import numpy as np


def Normalizing(df):
    scaler = MinMaxScaler()
    # Logging and Differencing
    df['natr'] = df['atr'] / df['Close']
    df['rsi'] = df['rsi'] / 100
    df['Close'] = np.log(df['Close']) - np.log(df['Close'].shift(1))
    df[['Close']] = scaler.fit_transform(df[['Close']])
    df = df[['Timestamp', 'Close', 'rsi', 'cmf', 'natr']]

    # column_names = ['Open', 'High', 'Low', 'Close', 'rsi', 'atr']
    return df


if __name__ == "__main__":
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', 1000)
    # testing normalization technieques
    df = pd.read_csv('./BTCUSDT_cycle2.csv')

    # df = df.dropna()
    # df = df.sort_values('time')

    # df["Close"] = df["Close"] - df["Close"].shift(1)
    df = df.rename(columns={'time': 'Timestamp', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close',
                            'volume': 'Volume'})


    df = AddIndicators(df)
    # print(df)
    df=df[100:]

    df = Normalizing(df)
    print(df)
    # df["atr"] = (df["atr"]) - (df["atr"].shift(1))

    # df["cmf"] = scaler.fit_transform(df["cmf"])


    # Min = df["Close"].min()
    # Max = df["Close"].max()
    # df["Close"] = (df["Close"] - Min) / (Max - Min)

    fig = plt.figure(figsize=(16, 8))
    plt.plot((df["Close"]))
    # plt.plot((df["vi_neg"]))
    # plt.plot(np.log(df["Close"]))

    ax = plt.gca()
    ax.grid(True)
    fig.tight_layout()
    plt.show()
