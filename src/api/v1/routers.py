from fastapi import APIRouter
from src.api.v1.endpoints.wallet import router as router_wallet

router = APIRouter()

router.include_router(router_wallet, prefix="/wallets", tags=["wallets"])
