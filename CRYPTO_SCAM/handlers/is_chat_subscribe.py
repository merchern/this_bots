from aiogram import types, Dispatcher
import markups as nav
from bot_data import bot, db, subscribe_chat_id, subscribe_chat_link, subscribe_chat_name, feedback_link, crypto_price_for_per, crypto_name, min_withdraw, bot_name
from decimal import *


async def is_subscribe(message: types.Message):

    user_channel_status = await bot.get_chat_member(chat_id=subscribe_chat_id, user_id=message.from_user.id)
    if user_channel_status["status"] != "left":
        await bot.send_message(message.from_user.id, "🥳 <b>Дарите подарки и зарабатывайте</b>\n\n"
                                                     f"<b>Отправляйте друзьям свою реферальную ссылку и получайте криптовалюту. Вывод станет доступен при накоплении</b> <code>{min_withdraw} {crypto_name}</code> <b>на балансе.</b>\n\n"
                                                     "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                                     "👤Ваша реферальная ссылка: "
                                                     f"<code>https://t.me/{bot_name}?start={message.from_user.id}</code>\n\n"
                                                     f"🚀Отзывы о нас: 👉 <a href='{feedback_link}'>Наши отзывы</a>\n"
                                                     "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                                     f"У вас {db.count_referrers(message.from_user.id)} подтвержденных рефералов\n"
                                                     f"Ваш баланс: <code>{db.get_client_data(message.from_user.id)[1]} {crypto_name} </code>  (<code>{Decimal(db.get_client_data(message.from_user.id)[1]) * Decimal(crypto_price_for_per)}$</code>)\n"
                                                     f"Ваш ID: <code>{message.from_user.id}</code>", parse_mode=types.ParseMode.HTML, disable_web_page_preview=True, reply_markup=nav.main_keyboard)
    else:
        try:
            await bot.delete_message(message_id=message.message_id, chat_id=message.from_user.id)
            await bot.send_message(message.from_user.id,
                                   "Чтобы начать получать криптовалюту, подпишитесь на канал. 👇\n\n"
                                   f"👉 <a href='{subscribe_chat_link}'>{subscribe_chat_name}</a>",
                                   parse_mode=types.ParseMode.HTML, reply_markup=nav.check_subscribe)
        except:
            await bot.send_message(message.from_user.id, "Чтобы начать получать криптовалюту, подпишитесь на канал. 👇\n\n"
                                                         f"👉 <a href='{subscribe_chat_link}'>{subscribe_chat_name}</a>", parse_mode=types.ParseMode.HTML, reply_markup=nav.check_subscribe)


async def check(call: types.CallbackQuery):
    await is_subscribe(call)
    await call.answer()


def register_handlers_subscribe(dp: Dispatcher):
    dp.register_message_handler(is_subscribe)
    dp.register_callback_query_handler(check, text_contains="check_subscribe")