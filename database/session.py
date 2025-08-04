from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./database.db"

# Создание движка
engine = create_async_engine(DATABASE_URL, echo=False)

# Сессия
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс моделей
Base = declarative_base()

# Функция для получения сессии
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

