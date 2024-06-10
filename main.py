from bot import bot
from jsonParser import getAllData
from handlers import client, admin, server

data = getAllData()

client.set_up_client(bot, data)
#admin.set_up_admin(bot, data)


bot.polling(none_stop=True)
