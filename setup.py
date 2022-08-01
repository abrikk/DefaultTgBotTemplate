from aiogram import Dispatcher
from aiogram_dialog import DialogRegistry

from tgbot.handlers.errors.error_handler import register_error_handler


def register_all_dialogs(dialog_registry: DialogRegistry):
    pass


def register_all_handlers(dp: Dispatcher):
    register_error_handler(dp)
