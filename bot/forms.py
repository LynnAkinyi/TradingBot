from django import forms
from .models import TradingBot

class TradingBotForm(forms.ModelForm):
    EXCHANGE_CHOICES = [
        ('BINANCE', 'Binance'),
        ('COINBASE', 'Coinbase'),
        ('KRAKEN', 'Kraken')
    ]
    
    PAIR_CHOICES = [
        ('BTCUSDT', 'BTC/USDT'),
        ('ETHUSDT', 'ETH/USDT'),
        ('BNBUSDT', 'BNB/USDT')
    ]
    
    exchange = forms.ChoiceField(choices=EXCHANGE_CHOICES)
    trading_pair = forms.ChoiceField(choices=PAIR_CHOICES)
    
    class Meta:
        model = TradingBot
        fields = ['name', 'exchange', 'trading_pair', 'api_key', 'api_secret']