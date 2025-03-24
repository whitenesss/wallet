from sqlalchemy import Integer, Float
from sqlalchemy.orm import Mapped, mapped_column


from src.database import Base


class Wallet(Base):
    __tablename__ = 'wallet'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    balance: Mapped[float] = mapped_column(Float, default=0.0)