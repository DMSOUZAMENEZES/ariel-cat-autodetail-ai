import asyncio
from decimal import Decimal
from uuid import uuid4

from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.models.service import Service
from app.models.tenant import Tenant
from app.models.user import User, UserRole

DEMO_TENANT_SLUG = "demo-detailing"

SERVICES = [
    ("Lavagem tecnica", "Lavagem detalhada externa com tecnica segura.", Decimal("120.00")),
    ("Higienizacao interna", "Limpeza e higienizacao completa do interior.", Decimal("280.00")),
    ("Polimento tecnico", "Correcao estetica de pintura com polimento tecnico.", Decimal("650.00")),
    ("Vitrificacao de pintura", "Protecao de pintura com coating vitrificador.", Decimal("1200.00")),
]


async def seed() -> None:
    async with AsyncSessionLocal() as session:
        tenant = await session.scalar(select(Tenant).where(Tenant.slug == DEMO_TENANT_SLUG))
        if tenant is None:
            tenant = Tenant(id=uuid4(), name="Demo Detailing", slug=DEMO_TENANT_SLUG)
            session.add(tenant)
            await session.flush()

        user = await session.scalar(select(User).where(User.email == "owner@example.com"))
        if user is None:
            session.add(
                User(
                    id=uuid4(),
                    tenant_id=tenant.id,
                    email="owner@example.com",
                    full_name="Demo Owner",
                    password_hash="not-for-production",
                    role=UserRole.owner,
                )
            )

        existing_service_names = set(
            await session.scalars(select(Service.name).where(Service.tenant_id == tenant.id))
        )
        for name, description, base_price in SERVICES:
            if name not in existing_service_names:
                session.add(
                    Service(
                        id=uuid4(),
                        tenant_id=tenant.id,
                        name=name,
                        description=description,
                        base_price=base_price,
                        currency="BRL",
                    )
                )

        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed())
