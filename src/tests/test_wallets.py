from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_create_wallet(client: AsyncClient):
    response = await client.post("/api/v1/wallets/create_wallet")
    assert response.status_code == 201
    data = response.json()
    assert "wallet_id" in data
    assert "balance" in data
    assert data["balance"] == "0.00"

@pytest.mark.asyncio
async def test_wallet_operations(client: AsyncClient):
    # Create wallet
    create_res = await client.post("/api/v1/wallets/create_wallet")
    wallet_id = create_res.json()["wallet_id"]

    # Deposit
    deposit = await client.post(
        f"/api/v1/wallets/{wallet_id}/operation",
        json={"operation_type": "DEPOSIT", "amount": "100.00"}
    )
    assert deposit.status_code == 200
    assert deposit.json()["new_balance"] == "100.00"

    # Withdraw
    withdraw = await client.post(
        f"/api/v1/wallets/{wallet_id}/operation",
        json={"operation_type": "WITHDRAW", "amount": "50.00"}
    )
    assert withdraw.status_code == 200
    assert withdraw.json()["new_balance"] == "50.00"
    # Test insufficient funds (Trying to withdraw more than the balance)
    withdraw_insufficient = await client.post(
        f"/api/v1/wallets/{wallet_id}/operation",
        json={"operation_type": "WITHDRAW", "amount": "200.00"}
    )
    assert withdraw_insufficient.status_code == 400
    assert withdraw_insufficient.json()["detail"] == "Insufficient funds"

