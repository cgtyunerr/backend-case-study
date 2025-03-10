"""Common mixins."""

from datetime import datetime
from typing import Annotated

from sqlalchemy import BIGINT, DateTime, String
from sqlalchemy.orm import Mapped, declarative_mixin, declared_attr, mapped_column

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


@declarative_mixin
class TableNameMixin:
    """Mixin for table_name."""

    @declared_attr
    def __tablename__(cls) -> str:
        """Generate table name."""
        return cls.__name__.lower()  # type: ignore[attr-defined]
