from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType

from config import TOKEN
from keyboards import contact_kb
from message import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_login(message: types.Message):
    await message.reply(say_hello, reply_markup=contact_kb)

@dp.message_handler(content_types=ContentType.CONTACT)
async def parsing(message: types.Message):
    from_user = message['from']
    chat = message['chat']
    contact = message['contact']
    if not from_user['is_bot']:
        if chat['id'] == contact['user_id'] == from_user['id']:
            await message.reply(nice_to_meet)
            user_card = {
                'user_first_name': contact['first_name'],
                'user_nick_name': from_user['username'],
                'user_last_name': contact['last_name'],
                'user_id': contact['user_id'],
                'user_phone_number': contact['phone_number']
            }
            print(user_card)
        else:
            await message.reply(you_are_pidor, reply_markup=contact_kb)




if __name__ == '__main__':
    executor.start_polling(dp)