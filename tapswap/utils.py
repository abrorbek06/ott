import telebot
from django.conf import settings
from telebot.apihelper import ApiTelegramException
import threading
import time
from django.db import models
from .models import UserCoin, RechargingSpeed

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, threaded=False)

def check_member(chat_id, user_id):
    link = '@' + chat_id.split('/')[-1] if not "@" in chat_id else chat_id
    try:
        member = bot.get_chat_member(link, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except ApiTelegramException:
        return False

def add_coins():
    users = UserCoin.objects.filter(max_coin__lt=models.F('limit'))

    for user in users:
        recharging_speed = RechargingSpeed.objects.get(user=user)

        # Tanga qo'shilish jarayoni
        if user.max_coin < user.limit:
            user.max_coin += recharging_speed.recharging_speed
            user.save()

def run_scheduler():
    while True:
        add_coins()  # Har bir siklda add_coins chaqiriladi
        time.sleep(1)  # 1 soniya kutish

def start_scheduler_in_thread():
    thread = threading.Thread(target=run_scheduler)
    thread.daemon = True
    thread.start()

start_scheduler_in_thread()
