from aiogram import types, Dispatcher
import markups as nav
from markups import cb
from handlers.is_chat_subscribe import is_subscribe
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from bot_data import bot, db, feedback_link, crypto_price_for_per, crypto_name, min_withdraw, bot_name
from decimal import *


class get_address(StatesGroup):
    address = State()
    confirm = State()


async def main_function(call: types.CallbackQuery, callback_data: dict):
    action = callback_data["action"]
    if action == "update_balance":
        try:
            await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                        text="🥳 <b>Дарите подарки и зарабатывайте</b>\n\n"
                                             f"<b>Отправляйте друзьям свою реферальную ссылку и получайте криптовалюту. Вывод станет доступен при накоплении</b> <code>{min_withdraw} {crypto_name}</code> <b>на балансе.</b>\n\n"
                                             "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                             "👤Ваша реферальная ссылка: "
                                             f"<code>https://t.me/{bot_name}?start={call.from_user.id}</code>\n\n"
                                             f"🚀Отзывы о нас: 👉 <a href='{feedback_link}'>Наши отзывы</a>\n"
                                             "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                             f"У вас {db.count_referrers(call.from_user.id)} подтвержденных рефералов\n"
                                             f"Ваш баланс: <code>{db.get_client_data(call.from_user.id)[1]} {crypto_name} </code>  (<code>{Decimal(db.get_client_data(call.from_user.id)[1]) * Decimal(crypto_price_for_per)}$</code>)\n"
                                             f"Ваш ID: <code>{call.from_user.id}</code>",
                                        parse_mode=types.ParseMode.HTML, disable_web_page_preview=True,
                                        reply_markup=nav.main_keyboard)
        except: pass

    if action == "withdraw_money":
        if Decimal(db.get_client_data(call.from_user.id)[1]) < Decimal(min_withdraw):
            await call.answer(f"У вас не достаточно денег для вывода\nМинимальная сумма вывода - {min_withdraw} {crypto_name}", show_alert=True)
        else:
            await bot.send_message(call.from_user.id, "Введите ваш криптокошелёк, чтобы вывести средства 👇")
            await get_address.address.set()

    await call.answer()


async def crypto_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address"] = message.text
    await bot.send_message(message.from_user.id, f"Это ваш адрес криптокошелька\n\n<b>{data['address']}</b>\n\n", reply_markup=nav.confirm_keyboard, parse_mode=types.ParseMode.HTML)
    await get_address.next()


async def crypto_confirm(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data["action"]
    current_state = await state.get_state()
    if current_state is None:
        return
    if action == "no":
        await bot.send_message(call.from_user.id, "Хорошо, можете ещё раз вывести средства и указать правильный адрес")
    if action == "yes":
        db.update_client_data(call.from_user.id, "0.0")
        await bot.send_message(call.from_user.id, "Все средства с вашего счета будут переведены на ваш адрес криптокошелька\n\nВ течение <b>1-7</b> рабочих дней", parse_mode=types.ParseMode.HTML)
    await state.finish()
    await call.answer()
    await is_subscribe(call)


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(main_function, cb.filter(action=["update_balance", "withdraw_money"]))
    dp.register_message_handler(crypto_address, state=get_address.address)
    dp.register_callback_query_handler(crypto_confirm, cb.filter(action=["no", "yes"]), state="*")