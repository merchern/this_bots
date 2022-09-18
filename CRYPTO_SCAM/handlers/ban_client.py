from aiogram import types, Dispatcher
from bot_data import bot, db, admin_chat
from handlers.is_chat_subscribe import is_subscribe


async def handler_for_ban_client(message: types.Message):
    if message.from_user.id in db.get_all_client_with_ban():
        await bot.send_message(message.from_user.id,
                               f"Ваша учетная запись была <b>заблокирована</b>. Все денежные средства на вашем счете были заморожены.\n\n"
                               f"Если вы считаете, что это ошибка и вы не нарушали ни одного правила.\n\nСвяжитесь с админом - @{admin_chat}",
                               parse_mode=types.ParseMode.HTML)
    else:
        await is_subscribe(message)


def register_handlers_ban_client(dp: Dispatcher):
    dp.register_message_handler(handler_for_ban_client)