import os

from telegram.ext import (
    CommandHandler,
    PicklePersistence,
    Updater
)

from tinkoff_bot.callbacks.start_callback import start

from tinkoff_bot.configuration import Config


def main() -> None:
    """Run the bot."""
    config = Config()

    persistence = PicklePersistence(
        filename='arbitrarycallbackdatabot.pickle', store_callback_data=True
    )

    updater = Updater(config.TELEGRAM_TOKEN, persistence=persistence, arbitrary_callback_data=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
