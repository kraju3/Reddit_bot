from flask import Flask
from nsbot import *
from log import States

bot = Flask(__name__)

@bot.route('/index')
def index():
    return 'Denied'

@bot.route('/telegram-update',methods=['POST'])
def telegram_update():
    incoming_messages(States.last_updated_id)


if __name__ == '__main__':
    States.last_updated_id = last_updated()
    bot.run()