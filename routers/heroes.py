# routers/heroes.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

# Importações da sua Lib
from HeroLib.models.models import Hero
from HeroLib.models.dto import HeroCreate, HeroPublic, HeroUpdate
from HeroLib.repository.repository import Repository
from HeroLib.service.service import Service
from HeroLib.util.database import SessionDep

# criar um router para agrupar as rotas de heróis 
router = APIRouter(
    prefix="/heroes",
    tags=["Heroes"]
)

# continua seguindo a lógica de antes, cria um repositório e um serviço pro herói poder ser manipulado, mas agora vem da lib 
hero_repo = Repository(Hero)
hero_service = Service(hero_repo)

# rotas CRUD para heróis
@router.post("/", response_model=HeroPublic, status_code=status.HTTP_201_CREATED)
def create_hero(session: SessionDep, hero_data: HeroCreate):
    """
    Cria um novo herói.
    """
    return hero_service.create(session, hero_data)

@router.get("/", response_model=List[HeroPublic])
def list_heroes(session: SessionDep, offset: int = 0, limit: int = 100):
    """
    Lista todos os heróis.
    """
    return hero_service.list(session, offset, limit)

@router.get("/{hero_id}", response_model=HeroPublic)
def get_hero(session: SessionDep, hero_id: int):
    """
    Obtém um herói específico pelo ID.
    """
    hero = hero_service.get(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Herói não encontrado")
    return hero

@router.patch("/{hero_id}", response_model=HeroPublic)
def update_hero(session: SessionDep, hero_id: int, hero_data: HeroUpdate):
    """
    Atualiza um herói (com o que o usuário quiser mudar).
    """
    try:
        updated_hero = hero_service.update(session, hero_id, hero_data)
        return updated_hero
    except ValueError:
        raise HTTPException(status_code=404, detail="Herói não encontrado")

@router.delete("/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hero(session: SessionDep, hero_id: int):
    """
    Deleta um herói.
    """
    try:
        hero_service.delete(session, hero_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Herói não encontrado")