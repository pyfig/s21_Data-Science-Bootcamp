Работа с .env файлами (ex06)

1. Подставляем значения в файл exampleENV
1.1 TOKEN_BOT = "EXAMPLE_VALUE" // Получаем от @BotFather
1.2 TOKEN_CHAT_ID = "EXAMPLE_VALUE" // Получаем от @get_id_bot
2. mv exampleENV .env
3. Выполняем команду `python send_message.py`
4. Done!

(!) Не забываем закоммитить .env файл в .gitignore
 