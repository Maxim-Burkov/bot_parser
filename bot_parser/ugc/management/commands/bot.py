import models
from django.conf import settings
from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext
from telegram.utils.request import Request


from ...models import Profile

# from .bot_parser.ugc.models import Profile
# from .bot_parser.ugc.models import Message


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'произошла ошибка: {e}'
            print(error_message)
            raise e
    return inner


@log_errors
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    reply_text = f'Ваш ib; {chat_id}'

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )

    update.message.reply_text(
        text=reply_text,
    )



class Command(BaseCommand):
    help = 'Телеграмм-бот'

    def handle(self, *args, **options):
        # 1----Правильное подключение
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
        )
        print(bot.get_me())
