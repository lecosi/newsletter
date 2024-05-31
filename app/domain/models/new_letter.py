from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey
)

from app.adapters.db.connection import Base


class Category(Base):
        __tablename__ = "categories"

        id = Column(Integer, primary_key=True, autoincrement=True)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, nullable=True)
        is_active = Column(Boolean, default=True)
        name = Column(String)


class NewLetter(Base):
    __tablename__ = "new_letters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    body = Column(Text, nullable=True)
    document_file = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    customer_email = Column(String)
    is_subscribed = Column(Boolean, default=True)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True)
    customer_email = Column(String)
    new_letter_id = Column(Integer, ForeignKey("new_letters.id"))
