import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Список аниме по жанрам
anime_data = {
    'Экшен': ['Атака Титанов', 'Ван-Панч Ман', 'Наруто', 'Блич', 'Моя геройская академия'],
    'Комедия': ['КоноСуба', 'Гинтама', 'Ван-Панч Ман', 'Сайки К', 'Лаки Стар'],
    'Романтика': ['Твоё имя', 'ТораДора!', 'Кланнад', 'Фрукты Baskets', 'Моя подростковая романтическая комедия SNAFU'],
    'Фантастика': ['Стейнс;Гейт', 'Ковбой Бибоп', 'Евангелион', 'Психо-Пасс', 'Призрак в доспехах'],
    'Драма': ['Твоя ложь в апреле', 'Анохана', 'Кланнад: После Истории', 'Март приходит как лев', 'Сделано в Бездне'],
    'Приключения': ['Охотник х Охотник', 'Ван Пис', 'Стальной алхимик: Братство', 'Мастера меча онлайн', 'Атака Титанов'],
    'Мистика': ['Обещанная Неверленд', 'Токийский гуль', 'Мушиши', 'Хигураши, когда плачут', 'Агент Паранойи']
}

async def start(update: Update, context) -> None:
    """Отправить сообщение при старте бота."""
    await update.message.reply_text(
        "Привет! Я помогу тебе найти аниме по жанру. Просто напиши жанр.\n"
        "Доступные жанры: Экшен, Комедия, Романтика, Фантастика, Драма, Приключения, Мистика\n"
        "Напиши 'выход', чтобы завершить."
    )

async def help_command(update: Update, context) -> None:
    """Отправить сообщение с инструкциями."""
    await update.message.reply_text("Напиши жанр аниме, и я порекомендую тебе случайное аниме!")

def get_anime_by_genre(genre):
    """Возвращает случайное аниме по жанру."""
    if genre in anime_data:
        return random.choice(anime_data[genre])
    else:
        return "Извините, я не знаю такого жанра."

async def handle_message(update: Update, context) -> None:
    """Обрабатывает текстовые сообщения."""
    user_input = update.message.text.strip().lower()

    if user_input == 'выход':
        await update.message.reply_text("До свидания!")
    else:
        response = get_anime_by_genre(user_input.capitalize())
        await update.message.reply_text(response)

def main() -> None:
    """Запуск бота."""
    # Вставьте сюда ваш API Token от BotFather
    application = Application.builder().token("7822710216:AAGq40G1CPMMQ9tx99IiNm2H9GdksD4Kbyg").build()

    # Команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Обработка сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
