import uuid
from enum import Enum
from decimal import Decimal
from pydantic import BaseModel, condecimal, Field


class OperationType(str, Enum):
    """
    Допустимые типы операций с кошельком
    """

    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class OperationRequest(BaseModel):
    """
    Схема для запроса на выполнение операции
    """

    operation_type: OperationType = Field(
        ..., title="Тип операции", description="Допустимые значения: DEPOSIT, WITHDRAW"
    )

    amount: condecimal(gt=0, decimal_places=2, max_digits=15) = Field(
        ...,
        title="Сумма",
        description="Положительное число с двумя знаками после запятой",
        example=100.50,
    )

    class Config:
        json_encoders = {Decimal: lambda v: f"{v:.2f}"}
        schema_extra = {"example": {"operation_type": "DEPOSIT", "amount": 150.75}}


class WalletResponse(BaseModel):
    """
    Схема для ответа с балансом кошелька
    """

    balance: Decimal = Field(
        ...,
        title="Баланс",
        description="Текущий баланс кошелька",
        example=2500.00,
        decimal_places=2,
    )

    class Config:
        json_encoders = {Decimal: lambda v: f"{v:.2f}"}


class OperationResponse(BaseModel):
    message: str
    new_balance: Decimal = Field(..., example=100.50)

    class Config:
        json_encoders = {Decimal: lambda v: f"{v:.2f}"}


class WalletAllResponse(BaseModel):
    wallet_id: uuid.UUID
    balance: Decimal = Field(
        ...,
        title="Баланс",
        description="Текущий баланс кошелька",
        example=2500.00,
        decimal_places=2,
    )
