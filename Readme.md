# Тестовый чат-бот для обработки заказа в Telegram
Бот реализован на фреймворке [aiogram](https://github.com/aiogram/aiogram)
<br>В качестве fsm используется [transitions](https://github.com/pytransitions/transitions)
<br>Ссылка на бота https://t.me/orders_9999999bot
* c помощью [@BotFather](https://telegram.me/BotFather) прописать для своего бота через /setcommands следующие команды:
  - start - старт диалога
  - help - помощь

### Инициализация на Heroku:
  ```bash
    heroku ps:scale bot=1
	heroku config:set TOKEN='<your_token>'
  ```