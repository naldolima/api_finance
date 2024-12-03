from pydantic import BaseModel
from datetime import datetime


class CreatePreco(BaseModel):
    ticker: str
    preco_real: float
    preco_previsto: float




class ShowPreco(BaseModel):
    ticker: str
    preco_real: float
    preco_previsto: float
    created_at: datetime
    class Config():
        orm_mode = True
