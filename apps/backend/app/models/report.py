from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Report(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "reports"

    tenant_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("tenants.id", ondelete="CASCADE"), index=True
    )
    evaluation_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("evaluations.id", ondelete="CASCADE"), index=True
    )
    title: Mapped[str] = mapped_column(String(180), nullable=False)
    payload: Mapped[dict] = mapped_column(JSONB, nullable=False)
    pdf_url: Mapped[str | None] = mapped_column(String(512))

    evaluation = relationship("Evaluation", back_populates="reports")
