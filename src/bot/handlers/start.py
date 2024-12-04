from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# from bot.keyboards.reply import menu_kb

start_router = Router()


@start_router.message(Command("start", "help", ignore_case=True, ignore_mention=True))
async def _command_help_handler(message: Message) -> None:
    """
    Handles the /start and /help commands by sending a list of available bot commands.
    """
    command_list = (
        "<b>Список команд бота:</b>\n"
        "<b><u>Администрация</u></b>\n"
        "/new_admin <i>@user</i> — <i>Дать права администратора</i>\n"
        "/revoke_admin <i>@user</i> — <i>Отобрать права администратора</i>\n"
        "/order — <i>Создать новую очередь</i>\n"
        "(reply) /del_order — <i>Удалить очередь</i>\n"
        "(reply) /del_user <i>q</i> — <i>Удалить человека из очереди</i>\n"
        "(reply) /mv <i>q1</i> <i>q2</i> — <i>Поменять места в очереди (q2=n+1 это конец очереди)</i>\n\n"
        "<b><u>Управление</u></b>\n"
        "(reply) /switch <i>q</i> — <i>Предложить пользователю поменяться местами</i>\n"
        "(reply) /upswitch <i>q</i> — <i>Предложить пользователю встать перед ним</i>\n"
        "(reply) /backswitch <i>q</i> — <i>Предложить пользователю встать за ним</i>\n"
        "q: (номер в очереди/<i>@user</i>), reply: ответ на сообщение бота"
    )
    await message.answer(command_list)
