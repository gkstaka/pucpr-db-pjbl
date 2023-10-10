from typing import Any

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __init__(self, **kw: Any):
        super().__init__(**kw)
