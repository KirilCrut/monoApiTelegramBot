# monoApiTelegramBot
# Бота можно использовать только в ограниченном кругу лиц, такие правила Monobank open API
Этот бот позволяет узнавать данные о счетах через Monobank open API(https://api.monobank.ua/docs/).
## Наглядный бот (без авторизации)
Актуально на 13.8.2021: https://t.me/monoapi_example_bot
## Функции бота
- Смотреть баланс счетов
- Смотреть курс валют
- Поддердивает нескольких пользователей, но только при ручном добавлении, такие условия использования Monobank open API
## Описание файлов
Название | Описание |
--- | --- |
main.py | Основной файл бота |
commands.py | Дополнительный скрипты |
keyboards.py | Клавиатуры для бота |
currency.py | Скрипт для парсинга курсов валют |
requirements.txt | Зависимости

## Установка
Скопируйте репозиторий:
    
    git clone https://github.com/KirilCrut/monoApiTelegramBot
Перейдите в папку:
    
    cd monoApiTelegramBot
Установите нужные библиотеки:
    
    pip install -r requirements.txt
Отдельно запустите парсер курсов валют (Я использую tmux):
  
    python3 currency.py
И запустите самого бота:

    python3 main.py
## Первый запуск:
Для первого запуска вам понадобится токен бота и ваш id, и после создаст файл конфига который вы сможете в любой момент изменить.

![first-run](https://i.imgur.com/40vEVMx.png)

Также создается база даных с доступом для админа и автоматически включает ему режим отладки.
## Основные команды
### Баланс `/balance`
Эта команда выводит баланс (а если включить режим отладки, то и статус запроса)

![balance](https://i.imgur.com/kfc3Nf6.png)
### Курс валют `/currency`
Эта команда показывает курс валют для Долларов, Евро и Рублей

![currency](https://i.imgur.com/11cX3lw.png)
## `/adduser`
Дает выбранному пользователю доступ к боту (бот вылетит если писать не цифры)
## Настройки `/options`
### Переключить режим отладки `/debug`
Переключает режим отладки
### Сбросить настройки `/reset`
Удаляет всю вашу информацию из бота (остается только доступ)
### Управление токеном `/tokenmenu`

![token-menu](https://i.imgur.com/rrxq2nz.png)
#### Просмотреть токен `/token`
Показывает ваш токен
#### Изменить токен `/changetoken`
Позволяет Добавить/Изменить токен в боте
#### Удалить токен `/deltoken`
Удаляет токен из бота
