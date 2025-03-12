"""Common mixins."""

from datetime import datetime
from typing import Annotated

from sqlalchemy import BIGINT, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

# Types
item_id = Annotated[
    int,
    mapped_column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
    ),
]

integer = Annotated[
    int,
    mapped_column(
        BIGINT,
        nullable=False,
    ),
]

text = Annotated[str, mapped_column(String, nullable=False)]

unique_text = Annotated[str, mapped_column(String, nullable=False, unique=True)]

# Mixins


class IdMixin:
    """Mixin for id."""

    id: Mapped[item_id]


class CreatedAtMixin:
    """Mixin for created_at."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
