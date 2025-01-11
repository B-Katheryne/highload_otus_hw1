import uuid
from sqlalchemy import Column, Date, String
from sqlalchemy_utils import UUIDType

from src.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)
    second_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    city = Column(String)
    biography = Column(String)
    birthdate = Column(Date)
    password = Column(String, nullable=False)
