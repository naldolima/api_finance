from typing import List
from fastapi import APIRouter, Depends, status,HTTPException
from db.models.user import User
from apis.v1.route_login import get_current_user
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.preco import treinar_modelo_preco,listar_resultado_modelo,delete_resultado_modelo
from schemas.preco import ShowPreco

router = APIRouter()

@router.get("")
def treinar_modelo(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    try:

        treinar_modelo_preco(db=db)

    except:
        raise HTTPException(
            detail="Error processing data",
            status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"Modelo treinado com sucesso"}

