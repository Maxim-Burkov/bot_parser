from django.core.management.base import BaseCommand

from django.conf import settings

from telegram import Bot
from telegram.utils.request import Request


class Command(BaseCommand):
    help = 'Телеграмм-бот'

    def handle(self, *args, **options):
        # Правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )
        print(bot.get_me())
