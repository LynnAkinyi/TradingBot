from django.db import models

class TradingBot(models.Model):
    name = models.CharField(max_length=100)
    exchange = models.CharField(max_length=50)
    api_key = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200)
    trading_pair = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    
class Trade(models.Model):
    bot = models.ForeignKey(TradingBot, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    side = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    amount = models.DecimalField(max_digits=20, decimal_places=8)