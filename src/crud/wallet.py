from decimal import Decimal
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from src.models.wallet import Wallet


class CRUDWallet:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_wallet_for_update(self, wallet_id: uuid.UUID) -> Wallet:
        wallet = await self.db.execute(
            select(Wallet).where(Wallet.id == wallet_id).with_for_update()
        )
        return wallet.scalar_one()

    async def get_wallet(self, wallet_id: uuid.UUID) -> Optional[Wallet]:
        wallet = await self.db.get(Wallet, wallet_id)
        return wallet

    async def get_all_wallets(self) -> list[Wallet]:
        result = await self.db.execute(select(Wallet))
        return result.scalars().all()

    async def create_wallet(self) -> Wallet:
        wallet = Wallet(balance=Decimal("0.00"))
        self.db.add(wallet)
        await self.db.commit()
        await self.db.refresh(wallet)
        return wallet

    async def update_balance(self, wallet: Wallet, amount: Decimal) -> None:
        wallet.balance += Decimal(amount)
        self.db.add(wallet)
        await self.db.commit()
        await self.db.refresh(wallet)
