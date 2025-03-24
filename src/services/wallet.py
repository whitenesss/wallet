import uuid
from decimal import Decimal

from fastapi import status, HTTPException

from src.crud.wallet import CRUDWallet
from src.models.wallet import Wallet
from src.schemas.wallet import OperationType


class WalletService:
    def __init__(self, crud: CRUDWallet):
        self.crud = crud

    async def get_all_wallets(self) -> list[Wallet]:
        return await self.crud.get_all_wallets()

    async def create_wallet(self) -> Wallet:
        return await self.crud.create_wallet()

    async def perform_operation(
        self, wallet_id: uuid.UUID, operation_type: OperationType, amount: Decimal
    ) -> Decimal:
        try:
            wallet = await self.crud.get_wallet_for_update(wallet_id)

            if operation_type == OperationType.WITHDRAW:
                self._validate_withdrawal(wallet, amount)
                amount = -amount

            await self.crud.update_balance(wallet, amount)
            return Decimal(wallet.balance)

        except Exception as e:
            raise self._handle_exception(e)

    async def get_balance(self, wallet_id: uuid.UUID) -> Decimal:
        wallet = await self.crud.get_wallet(wallet_id)
        if not wallet:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Wallet not found"
            )
        return Decimal(wallet.balance)

    def _validate_withdrawal(self, wallet: Wallet, amount: Decimal):
        if wallet.balance < amount:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds"
            )

    def _handle_exception(self, error: Exception):
        if isinstance(error, HTTPException):
            return error
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
