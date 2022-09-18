from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.data import Database

db = Database("data.db")
# ___________________________________________________________________
admin_id = [123]  # Сюда вставляем всех админов через запятую [123123, 837148, 12312] или только одного [123]
token = "1238453:AAH2wl3hIHFDLA"  # токен бота

subscribe_chat_id = -12312314  # Id канал, на который нужно подписаться. Предварительно нужно добавить бота в администраторы
admin_chat = "WhoAreU"  # username админа без @ для связи

bot_name = "WOW"  # username бота без @ для генерации ссылок

# Все цифры ниже в виде строки!

crypto_price_for_per = "10"  # цена за 1 даваемою криптовалюту в $(пример: 1 doge - 0.1 $) --> crypto_price_for_per = 0.1
crypto_name = "DOGE"  # Название криптовалюты
min_withdraw = "10.0"  # Минимальная сумма вывода

crypto_for_per_referral = "0.5"  # сколько криптовалюты дается за каждого реферала

subscribe_chat_name = "Test_NFT"  # название чата, на который нужно подписаться
subscribe_chat_link = "https://t.me/maybelink"  # ссылка на чат, на который нужно подписаться
feedback_link = "https://yandex.ru"  # ссылка на канал/сайт с отзывами
# ___________________________________________________________________

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)