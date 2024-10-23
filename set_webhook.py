import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tapswap.settings')

django.setup()

from tapswap.utils import bot
from tapswap.settings import BACKEND_URL

def web():
    bot.remove_webhook()
    bot.set_webhook(url=f"{BACKEND_URL}name/")

if __name__ == "__main__":
    web()
    info = bot.get_webhook_info()
    print(info)

#python3 set_webhook.py