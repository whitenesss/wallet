import uuid
from fastapi import APIRouter, Depends, status, HTTPException
from src.dependencies import get_wallet_service
from src.schemas.wallet import OperationRequest, OperationResponse, WalletAllResponse
from src.services.wallet import WalletService

router = APIRouter()


@router.post(
    "/{wallet_uuid}/operation",
    response_model=OperationResponse,
    status_code=status.HTTP_200_OK,
)
async def perform_operation(
    wallet_uuid: uuid.UUID,
    operation: OperationRequest,
    service: WalletService = Depends(get_wallet_service),
):
    new_balance = await service.perform_operation(
        wallet_id=wallet_uuid,
        operation_type=operation.operation_type,
        amount=operation.amount,
    )
    return {"message": "Operation successful", "new_balance": new_balance}


@router.post(
    "/create_wallet",
    response_model=WalletAllResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_wallet(service: WalletService = Depends(get_wallet_service)):
    wallet = await service.create_wallet()
    return {"wallet_id": wallet.id, "balance": wallet.balance}


@router.get(
    "/get_all", response_model=list[WalletAllResponse], status_code=status.HTTP_200_OK
)
async def get_all_wallets(service: WalletService = Depends(get_wallet_service)):
    wallets = await service.get_all_wallets()
    return [{"wallet_id": wallet.id, "balance": wallet.balance} for wallet in wallets]

