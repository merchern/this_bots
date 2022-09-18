from aiogram import executor
from handlers import client, ban_client, is_chat_subscribe, referral, admin
from bot_data import dp


async def on_startup(_):
    print("Bot Started")


admin.register_handlers_admin(dp)
referral.register_handlers_referral(dp)
ban_client.register_handlers_ban_client(dp)
is_chat_subscribe.register_handlers_subscribe(dp)
client.register_handlers_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)