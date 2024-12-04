from aiogram.filters import Filter
from aiogram.types import Message

from bot.config import config


class IsOwner(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in config.OWNER_IDS
