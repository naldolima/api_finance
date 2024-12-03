from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(...,min_length=4)
    is_admin: bool = False

class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_admin: bool
    is_active: bool

    class Config():
        orm_mode = True

