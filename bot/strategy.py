import pandas as pd
import numpy as np

class Strategy:
    def __init__(self, client):
        self.client = client
    
    def simple_moving_average(self, symbol, short_window=20, long_window=50):
        ohlcv = self.client.exchange.fetch_ohlcv(symbol, '1m')
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        df['SMA_short'] = df['close'].rolling(window=short_window).mean()
        df['SMA_long'] = df['close'].rolling(window=long_window).mean()
        
        if df['SMA_short'].iloc[-1] > df['SMA_long'].iloc[-1] and \
           df['SMA_short'].iloc[-2] <= df['SMA_long'].iloc[-2]:
            return 'buy'
        elif df['SMA_short'].iloc[-1] < df['SMA_long'].iloc[-1] and \
             df['SMA_short'].iloc[-2] >= df['SMA_long'].iloc[-2]:
            return 'sell'
        return None