from telebot import types
from jsonParser import changeData

async def set_up_admin(bot, data):
    pass
    # @bot.message_handler(commands=['admin'])
    # def admin(message):
    #     if message.chat.id == int(data['adminChatId']):
    #         keyboard = data['keyboards']['keyBoardAdmin']
    #
    #         markup = types.InlineKeyboardMarkup()
    #         markup.add(types.InlineKeyboardButton(text=keyboard['changeData'][0],
    #                                               callback_data="change"))
    #         markup.add(types.InlineKeyboardButton(text=keyboard['openHelp'][0],
    #                                               callback_data=keyboard['openHelp'][1]))
    #         markup.add(types.InlineKeyboardButton(text="text",
    #                                               callback_data="hi"))
    #
    #         bot.send_message(message.chat.id, keyboard['titleMenu'], reply_markup=markup)
    #
    # def help_message():
    #     pass

    # @bot.callback_query_handler(func=lambda call: True)
    # def callback_worker(call):
    #     keyboardAdmin = data['keyboards']['keyBoardAdmin']
    #     keyboardClient = data['keyboards']['keyBoardMenu']
    #
    #     if call.data == "hi":
    #         print("я перешел")
    #
    #     if call.data == "change":
    #         print("я перешел")
    #         markup = types.InlineKeyboardMarkup()
    #         markup.add(types.InlineKeyboardButton(text=keyboardClient['whenMessage'][0],
    #                                               callback_data=keyboardClient['whenMessage'][1]))
    #         markup.add(types.InlineKeyboardButton(text=keyboardClient['prefixMessage'][0],
    #                                               callback_data=keyboardClient['prefixMessage'][1]))
    #         markup.add(types.InlineKeyboardButton(text=keyboardClient['rulesMessage'][0],
    #                                               callback_data=keyboardClient['rulesMessage'][1]))
    #         markup.add(types.InlineKeyboardButton(text=keyboardClient['helpMessage'][0],
    #                                               callback_data=keyboardClient['helpMessage'][1]))
    #         markup.add(types.InlineKeyboardButton(text=keyboardClient['socialMessage'][0],
    #                                               callback_data=keyboardClient['socialMessage'][1]))
    #         markup.add(types.InlineKeyboardButton(text=data['backMessage'],
    #                                               callback_data="menu"))
    #
    #         bot.send_message(call.message.chat.id, keyboardAdmin['changeData'][2], reply_markup=markup)
    #
    #     if call.data == "1":
    #         bot.send_message(call.message.chat.id, keyboardAdmin['currentData'])
    #         bot.send_message(call.message.chat.id, data['whenMessage'])
    #
    #         def change_data(message):
    #             change(message, data['whenMessage'])
    #
    #         bot.register_next_step_handler(call.message, change_data)
    #
    #         bot.send_message(call.message.chat.id, text="Новые данные:\n"+data['whenMessage'])
    #
    #
    # def change(message, inf):
    #     newData = message.text
    #
    #     inf = newData
    #
    #     changeData(inf, 4)





