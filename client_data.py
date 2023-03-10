from bot_telegram import dp, bot, types


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Хорошего времяпрепровождения') #здесь отправляем клавиатуру клиенту