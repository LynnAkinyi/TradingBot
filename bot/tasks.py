from celery import shared_task
from .models import TradingBot
from .exchange import ExchangeClient
from .strategy import Strategy

@shared_task
def run_trading_bot(bot_id):
    bot = TradingBot.objects.get(id=bot_id)
    client = ExchangeClient(bot.exchange, bot.api_key, bot.api_secret)
    strategy = Strategy(client)
    
    while bot.is_active:
        try:
            signal = strategy.simple_moving_average(bot.trading_pair)
            if signal:
                balance = client.get_balance('USDT')
                if signal == 'buy' and balance > 0:
                    client.create_order(bot.trading_pair, 'market', 'buy', balance * 0.95)
                elif signal == 'sell':
                    balance = client.get_balance(bot.trading_pair.split('/')[0])
                    if balance > 0:
                        client.create_order(bot.trading_pair, 'market', 'sell', balance)
        except Exception as e:
            print(f"Error: {str(e)}")
            break