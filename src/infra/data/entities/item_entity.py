from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.database.pg_adapter import Base


class ItemEntity(Base):
    __tablename__ = "items"

    item_id: Mapped[int] = mapped_column(
        "item_id", Integer, nullable=False, unique=True, primary_key=True
    )
    name: Mapped[str] = mapped_column("name", String(length=64), nullable=False)
    email: Mapped[str] = mapped_column("email", String(length=64), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column("updated_at", DateTime, nullable=False)
    created_at: Mapped[DateTime] = mapped_column("created_at", DateTime, nullable=False)
