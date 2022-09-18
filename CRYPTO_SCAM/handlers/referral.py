from aiogram import types, Dispatcher
from bot_data import bot, db,crypto_name, crypto_for_per_referral
from decimal import *
from handlers.is_chat_subscribe import is_subscribe
from handlers.ban_client import handler_for_ban_client


async def register_referral(message: types.Message):
    if message.from_user.id not in db.get_all_client_with_ban():
        if not db.user_exists(message.from_user.id):
            referrer_id = str(message.text[7:])
            if referrer_id != "":
                if referrer_id != str(message.from_user.id):
                    db.add_client(message.from_user.id)
                    db.add_referral(user_id=message.from_user.id, referrer_id=referrer_id)
                    try:
                        db.update_client_data(referrer_id, str(Decimal(db.get_client_data(referrer_id)[1]) + Decimal(crypto_for_per_referral)))
                        await bot.send_message(int(referrer_id), f"🎉 У вас новый реферал(<code>@{message.from_user.username if message.from_user.username is not None else 'Noname'}</code>),"
                                                                 f" ваш баланс пополнен на {crypto_for_per_referral} {crypto_name}\n\n На вашем балансе {db.get_client_data(referrer_id)[1]} {crypto_name}",
                                               parse_mode=types.ParseMode.HTML)
                    except: pass
                    await is_subscribe(message)
                else:
                    await bot.send_message(message.from_user.id, "Это ваша же ссылка 😰")
            else:
                db.add_client(message.from_user.id)
                await is_subscribe(message)
        else:
            await is_subscribe(message)
    else:
        await handler_for_ban_client(message)


def register_handlers_referral(dp: Dispatcher):
    dp.register_message_handler(register_referral, commands=["start"])