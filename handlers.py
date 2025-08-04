from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from database.session import get_session
from database.models import User

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    async with get_session() as session:
        user = await session.get(User, message.from_user.id)

        if not user:
            new_user = User(
                id=message.from_user.id,
                username=message.from_user.username,
                full_name=message.from_user.full_name
            )
            session.add(new_user)
            await session.commit()
            await message.answer(f"Привет, {message.from_user.full_name}! Ты добавлен в базу.")
        else:
            await message.answer(f"С возвращением, {message.from_user.full_name}!")

