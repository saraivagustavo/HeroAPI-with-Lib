from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

# Importações da sua Lib
from HeroLib.models.models import Team
from HeroLib.models.dto import TeamCreate, TeamPublic
from HeroLib.repository.repository import Repository
from HeroLib.service.service import Service
from HeroLib.util.database import SessionDep

# mesma lógica do heroes.py, mas agora para times
router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)

# mesma lógica do heroes.py, mas agora para times
team_repo = Repository(Team)
team_service = Service(team_repo)

# rotas CRUD para times
@router.post("/", response_model=TeamPublic, status_code=status.HTTP_201_CREATED)
def create_team(session: SessionDep, team_data: TeamCreate):
    """
    Cria um novo time.
    """
    return team_service.create(session, team_data)

@router.get("/", response_model=List[TeamPublic])
def list_teams(session: SessionDep, offset: int = 0, limit: int = 100):
    """
    Lista todos os times.
    """
    return team_service.list(session, offset, limit)