from typing import List

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    CallbackContext,
    Updater,
)

from tinkoff_bot.const import (
    START_MESSAGE
)


def start(update: Update, context: CallbackContext) -> None:
    number_list: List[int] = []
    update.message.reply_text(START_MESSAGE, reply_markup=build_keyboard(number_list))


def build_keyboard(current_list: List[int]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton(str(i), callback_data=(i, current_list)) for i in range(1, 6)]
    )