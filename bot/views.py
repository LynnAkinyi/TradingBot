from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TradingBot
from .forms import TradingBotForm
from .tasks import run_trading_bot
from redis.exceptions import ConnectionError

def bot_list(request):
    try:
        bots = TradingBot.objects.all().prefetch_related('trade_set')
        context = {'bots': bots}
    except Exception as e:
        messages.error(request, f'Error loading bots: {str(e)}')
        context = {'bots': []}
    return render(request, 'bot/bot_list.html', context)

def bot_create(request):
    if request.method == 'POST':
        form = TradingBotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bot_list')
    else:
        form = TradingBotForm()
    return render(request, 'bot/bot_create.html', {'form': form})

def bot_start(request, bot_id):
    try:
        bot = TradingBot.objects.get(id=bot_id)
        bot.is_active = True
        bot.save()
        run_trading_bot.delay(bot_id)
        messages.success(request, f'Bot {bot.name} started successfully')
    except ConnectionError:
        messages.error(request, 'Redis connection failed. Please check Redis server.')
        bot.is_active = False
        bot.save()
    except Exception as e:
        messages.error(request, f'Error starting bot: {str(e)}')
        bot.is_active = False
        bot.save()
    return redirect('bot_list')

def bot_stop(request, bot_id):
    bot = TradingBot.objects.get(id=bot_id)
    bot.is_active = False
    bot.save()
    return redirect('bot_list')