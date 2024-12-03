from sqlalchemy.orm import Session
from modelos.lstm import get_model
from db.models.preco import Preco
from core.config import settings


def treinar_modelo_preco(db: Session):
    result_modelo = get_model(settings.DT_START_TRAIN,settings.DT_END_TRAIN,settings.DT_START_VALID,settings.DT_END_VALID,settings.NUM_EXAMPLES,settings.VAL_SIZE)
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
