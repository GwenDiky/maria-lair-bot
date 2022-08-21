from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random 
import datetime
import logging
from telegram import __version__ as TG_VER
import schedule
import time 
import config 


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ > (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )




# show errors
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)



def start(update, context):
    update.message.reply_text('ты у меня самая лучшая а они тьфу никто и пустой звон')
    

def help(update, context):
    update.message.reply_text('ну и чем я тебе могу помочь бессоветное создание\nкоманды: \n/start \n/help \n/psycho')

def error(update, context):
    update.message.reply_text('ох...')

def text(update, context):
    text_list = ['если что тебе все еще нельзя открыто проявлять свое доброе отношение к другим лбдям а-то вдруг кто-то кирпичом даст', 'не думай индюк думал и в суп попал', 'спасибо радость моя', 'какая же ты отвртаильнач', 'ты самая лучшая самая прекрасная', 
    'смешная ты еп твою мать', 'ох как же я люблю комплименты', 'доброта - это посредственное качество', 'подлый алекситимик', 'если вы умрёте не естественной смертью это будет с вероятностью 80% от моих рук', 
    'ляллялялялялялялял', 'смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть смерть', 
    'конечно конечно ты самый добрый человек как же может быть иначе', 'да ты у меня самая лучшая', 'да точно ненормальная', 'да\nи что\nа ой\nнет\nне правда',
    'я общаюсь с каким-то монстром', 'раздели мои страдания', 'если ты умрёшь то или от естественной смерти в моих руках или от моих рук в моих руках', 
    'фу блять выкинь эту идею из своей головы']
    text_receives = update.message.text 
    text_receives.lower()
    if "привет" in text_receives:
        update.message.reply_text('привет зайчик')
    elif "дела" in text_receives:
        update.message.reply_text('я буду счастлива когда артем умрет')
    elif ("плохо" or "умираю") in text_receives:
        update.message.reply_text('тебе рано умирать твой отец еще жив')
    elif "скучно" in text_receives:
        update.message.reply_text('найди себе жертву ляляля')
    elif "егор" in text_receives: 
        update.message.reply_text("хуйлан")
    else: 
        update.message.reply_text(random.choice(text_list))

def psycho(update, context):
    future = datetime.date(2022, 11, 3)
    today = datetime.date.today()
    psycho = (future-today).days
    update.message.reply_text(f'до начала твоего общения с психопатами осталось {psycho} дней')


def callback_auto_message(context, update):
    context.bot.send_message(chat_id=update.effective_chat.id, text='как ты котик мой?')


def start_auto_messaging(update, context):
    chat_id = update.message.chat_id
    context.job_queue.run_daily(callback_auto_message, time=datetime.time(hour=20, minute=0), days=(0, 1, 2, 3, 4, 5, 6), context=chat_id)

"""def send_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="как ты котик мой?")
schedule.every().day.at("19:05").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
"""
    

def main():
    TOKEN = config.TOKEN
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("psycho", psycho))
    dispatcher.add_handler(CommandHandler("auto", start_auto_messaging))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)
   
    updater.start_polling()
    # run the bot until Ctrl-C
    updater.idle()
if __name__ == '__main__':
    main()