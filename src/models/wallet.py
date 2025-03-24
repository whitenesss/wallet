import uuid
from sqlalchemy import Numeric, UUID
import uuid
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column


from src.database import Base


class Wallet(Base):
    __tablename__ = "wallets"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    balance: Mapped[Decimal] = mapped_column(
        Numeric(precision=15, scale=2), default=Decimal("0.00"), nullable=False
    )
