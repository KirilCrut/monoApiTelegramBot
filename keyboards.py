import telebot
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Баланс')
keyboard.row('Настройки')

keyboardOpt = telebot.types.ReplyKeyboardMarkup(True)
keyboardOpt.row('Управление токеном')
keyboardOpt.row('Сбросить настройки')
keyboardOpt.row('Назад')

keyboardToken = telebot.types.ReplyKeyboardMarkup(True)
keyboardToken.row('Просмотреть токен')
keyboardToken.row('Изменить токен')
keyboardToken.row('Удалить токен')
keyboardToken.row('Назад')

keyboardDelToken = telebot.types.ReplyKeyboardMarkup(True)
keyboardDelToken.row('Да', 'Нет')

keyboardBack = telebot.types.ReplyKeyboardMarkup(True)
keyboardBack.row('Назад')