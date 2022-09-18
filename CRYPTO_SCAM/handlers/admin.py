from aiogram import types, Dispatcher
from bot_data import bot, db, admin_id


async def admin_commands(message: types.Message):
    if message.text[1:2] == "u":
        if message.text[7:].isdigit():
            if db.client_exist(message.text[7:]):
                try:
                    db.unban_client(message.text[7:])
                    await bot.send_message(message.from_user.id, f"Пользователь {message.text[7:]} был успешно разбанин",)
                except: await bot.send_message(message.from_user.id, "Произошла ошибка, проверьте id")
            else:
                await bot.send_message(message.from_user.id, "Такого пользователя нету")
        else:
            await bot.send_message(message.from_user.id, "ID должен состоять из цифр")
    if message.text[1:2] == "b":
        if message.text[5:].isdigit():
            if db.client_exist(message.text[5:]):
                try:
                    db.ban_client(message.text[5:])
                    await bot.send_message(message.from_user.id, f"Пользователь {message.text[5:]} был успешно забанин",)
                except: await bot.send_message(message.from_user.id, "Произошла ошибка, проверьте id")
            else:
                await bot.send_message(message.from_user.id, "Такого пользователя нету")
        else:
            await bot.send_message(message.from_user.id, "ID должен состоять из цифр")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_commands, user_id=admin_id, commands=["unban", "ban"])