import uvicorn
from fastapi import FastAPI
from HeroLib.util.database import init_db
from routers import heroes, teams

app = FastAPI(
    title="API de Heróis e Times",
    description="Uma API para gerenciar Heróis e Times usando a HeroLibSaraiva",
    version="1.0.0"
)

init_db()

app.include_router(heroes.router)
app.include_router(teams.router)

@app.get("/", tags=["Root"])
def health():
    """
    Rota principal da API.
    """
    return {"mensagem": "Bem-vindo à API de Heróis! Acesse /docs para documentação."}
