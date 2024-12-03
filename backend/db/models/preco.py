from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from db.base_class import Base

class Preco(Base):
    id = Column(Integer, primary_key=True)
    ticker = Column(String,nullable=True)
    data = Column(DateTime,nullable=True)
    preco_real = Column(Float, nullable=True)
    preco_previsto = Column(Float, nullable=True)
    created_at = Column(DateTime,default=datetime.now())

