from telebot import types


def set_up_client(bot, data):
    @bot.message_handler(commands=['start', 'menu'])
    def start(message):

        startMessage = data['messages']['startMessage']
        bot.send_message(message.chat.id, startMessage)

        menu(message, data)

    @bot.message_handler(commands=['menu'])
    def menu(message, data):
        keyBoardMenu = data['keyboards']['keyBoardMenu']

        keyBoard = types.InlineKeyboardMarkup()
        keyBoard.add(types.InlineKeyboardButton(text=keyBoardMenu['whenMessage'][0],
                                                callback_data=keyBoardMenu['whenMessage'][1]))
        keyBoard.add(types.InlineKeyboardButton(text=keyBoardMenu['prefixMessage'][0],
                                                callback_data=keyBoardMenu['prefixMessage'][1]))

        keyBoard.add(types.InlineKeyboardButton(text=keyBoardMenu['rulesMessage'][0],
                                                callback_data=keyBoardMenu['rulesMessage'][1]))
        keyBoard.add(types.InlineKeyboardButton(text=keyBoardMenu['helpMessage'][0],
                                                callback_data=keyBoardMenu['helpMessage'][1]))
        keyBoard.add(types.InlineKeyboardButton(text=keyBoardMenu['socialMessage'][0],
                                                callback_data=keyBoardMenu['socialMessage'][1]))

        bot.send_message(message.chat.id, keyBoardMenu['titleMenu'], reply_markup=keyBoard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):

        if '|' in call.data:
            callName = call.data.split('|')[0]

            chatId = call.data.split('|')[1]


        else:
            callName = call.data

        keyBoardMenu = data['keyboards']['keyBoardMenu']

        keyBoard = types.InlineKeyboardMarkup()
        keyBoard.add(types.InlineKeyboardButton(data['messages']['backMessage'], callback_data='menu'))

        if callName == keyBoardMenu['whenMessage'][1]:
            bot.send_message(call.message.chat.id, data['messages']['whenMessage'], reply_markup=keyBoard)

        if callName == keyBoardMenu['prefixMessage'][1]:
            bot.send_message(call.message.chat.id, data['messages']['prefixMessage'], reply_markup=keyBoard)

        if callName == keyBoardMenu['rulesMessage'][1]:
            bot.send_message(call.message.chat.id, data['messages']['rulesMessage'], reply_markup=keyBoard)

        if callName == keyBoardMenu['helpMessage'][1]:
            bot.send_message(call.message.chat.id, data['messages']['helpMessage'], reply_markup=keyBoard)

            def sendMessage(message):
                if message.chat.id != int(data['adminChatId']):
                    send_to_help(message)

            bot.register_next_step_handler(call.message, sendMessage)

        if callName == keyBoardMenu['socialMessage'][1]:
            socialNetworkMessage = data['messages']['socialMessage']
            instUrl = data['instUrl']
            tgUrl = data['tgUrl']
            tiktokUrl = data['tiktokUrl']

            instButton = types.InlineKeyboardButton("Instagram", url=instUrl)
            tgButton = types.InlineKeyboardButton("Telegram", url=tgUrl)
            tiktokButton = types.InlineKeyboardButton("TikTok", url=tiktokUrl)

            markup = types.InlineKeyboardMarkup()
            markup.add(instButton)
            markup.add(tgButton)
            markup.add(tiktokButton)
            markup.add(types.InlineKeyboardButton(text=data['messages']['backMessage'], callback_data='menu'))

            bot.send_message(call.message.chat.id, socialNetworkMessage, reply_markup=markup)

        if callName == "menu":
            menu(call.message, data)

        if callName == "answer":
            bot.send_message(call.message.chat.id, "Напишите ответ этому пользователю ниже:")

            def answer(message):

                textAnswer = message.text

                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Вернуться назад", callback_data="menu"))
                bot.send_message(chat_id=chatId, text=f"Пришло сообщнеие от поддержки: \n\n"
                                                      f"{textAnswer}",
                                 reply_markup=markup)

            bot.register_next_step_handler(call.message, answer)


    @bot.message_handler(commands=['whatiD'])
    def check(message):
        bot.send_message(message.chat.id, message.chat.id)

    def send_to_help(message):

        markup = types.InlineKeyboardMarkup()
        tmp = str("answer" + "|" + str(message.chat.id) + '|' + str(message.from_user.id))
        markup.add(types.InlineKeyboardButton("Ответить", callback_data=tmp))
        bot.send_message(data['adminChatId'], f"Пришло новое сообщение\n\n"
                                              f"Chat Id: {message.chat.id}\n"
                                              f"UserName: @{message.from_user.username}\n\n"
                                              f"Text: {message.text}",
                         reply_markup=markup)
