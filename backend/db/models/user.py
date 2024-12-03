from db.base_class import Base
from sqlalchemy import Boolean, Column,Integer,String

class User(Base):
    id = Column(Integer,primary_key=True, index=True)
    email = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean,default=True)
