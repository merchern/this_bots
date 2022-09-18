from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData("fabnum", "action")

# ________________________________________________
check_subscribe = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton("🔍 Проверить подписку", callback_data="check_subscribe"))

main_keyboard = InlineKeyboardMarkup(row_width=2)
main_keyboard.row(InlineKeyboardButton("🔄 Обновить баланс", callback_data=cb.new(action="update_balance")), InlineKeyboardButton("📥 Вывод средств", callback_data=cb.new(action="withdraw_money")))

confirm_keyboard = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton("Да", callback_data=cb.new(action="yes")), InlineKeyboardButton("Нет", callback_data=cb.new(action="no")))
