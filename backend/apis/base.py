from fastapi import APIRouter
from apis.v1 import route_user
from apis.v1 import route_login
from apis.v1 import route_preco
from apis.v1 import route_listar_preco


api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/users", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
api_router.include_router(route_preco.router, prefix="/treinar_modelo", tags=["treinar_modelo"])
api_router.include_router(route_listar_preco.router, prefix="/listar_modelo", tags=["listar_modelo"])


