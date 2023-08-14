from aiogram import types

START_MESSAGE = "Бот активирован"


def get_me_message(message: types.Message) -> str:
    arguments = message.get_args()
    user = message.from_user
    if user.first_name:
        return f"{user.first_name} {arguments}"
    if user.username:
        return f"{user.username} {arguments}"
    # А если у пользователя нет ни имени, ни ника? Ситуация редкая, но надо обработать.
    return "message"
