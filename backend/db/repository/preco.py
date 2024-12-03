from sqlalchemy.orm import Session
from modelos.lstm import get_model
from db.models.preco import Preco
from core.config import settings
from datetime import datetime

def treinar_modelo_preco(db: Session):
    result_modelo = get_model('2024-06-01', '2024-09-01', '2024-09-01', '2024-11-01', 1, 5)

    delete_resultado_modelo(db=db)

    for i, infos in result_modelo.iterrows():
        preco = Preco(
            ticker=infos.unique_id,
            data=infos.ds,
            preco_real=infos.y,
            preco_previsto=infos.AutoLSTM
            )
        db.add(preco)
        db.commit()
        db.refresh(preco)
    return 'Modelo treinado com sucesso'

def listar_resultado_modelo(db: Session):
    preco = db.query(Preco).all()
    return preco

def delete_resultado_modelo(db: Session):
    db.query(Preco).delete()
    db.commit()
