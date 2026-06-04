from uuid import UUID

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class AuditLog(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "audit_logs"

    tenant_id: Mapped[UUID | None] = mapped_column(PG_UUID(as_uuid=True), index=True)
    actor_user_id: Mapped[UUID | None] = mapped_column(PG_UUID(as_uuid=True), index=True)
    action: Mapped[str] = mapped_column(String(120), nullable=False)
    entity_type: Mapped[str | None] = mapped_column(String(120))
    entity_id: Mapped[UUID | None] = mapped_column(PG_UUID(as_uuid=True))
    metadata_json: Mapped[dict | None] = mapped_column(JSONB)
