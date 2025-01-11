from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.base import get_session

DB = Annotated[AsyncSession, Depends(get_session)]
