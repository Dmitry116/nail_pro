from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет' or message.text == 'привет':
        await message.answer('Хочешь педикюр?')  # передаем то что хотим отправить обратно
    # await message.reply(message.text)   #упоменает сообщение на которое отвечает
    # await bot.send_message(message.from_user.id, message.text)  #бот пишет пользователю в личку(если пользователь написал боту первым)


executor.start_polling(dp, skip_updates=True)
