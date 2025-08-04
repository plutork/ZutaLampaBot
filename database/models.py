from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Boolean
from database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    date_time = Column(DateTime)
    price = Column(Integer, default=0)
