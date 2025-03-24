from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.database import get_db
from src.crud.wallet import CRUDWallet
from src.services.wallet import WalletService


# 1. Зависимость для CRUD
async def get_crud(db: AsyncSession = Depends(get_db)) -> CRUDWallet:
    return CRUDWallet(db)


# 2. Зависимость для сервиса
async def get_wallet_service(crud: CRUDWallet = Depends(get_crud)) -> WalletService:
    return WalletService(crud)
