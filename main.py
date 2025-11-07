import uvicorn
from fastapi import FastAPI
from HeroLib.util.database import init_db
from routers import heroes, teams

descricao = """
## 📖 Visão Geral do Projeto
Esta API, desenvolvida com **FastAPI**, expõe endpoints para o cadastro de **Heróis** e seus múltiplos **Times**.

O projeto atua como a camada de **Controller** (ou "View" no MVC), consumindo uma biblioteca externa (`HEROLIBsaraivagustavo`) que abstrai toda a lógica de negócios e acesso a dados.

---

### 🏛️ Arquitetura e Padrões
A arquitetura é desacoplada, separando claramente as responsabilidades:

* **Controller (`Esta API`)**: Implementada com `APIRouter` do FastAPI. Esta camada é responsável por expor os *endpoints*, receber as requisições HTTP e retornar as respostas.

* **Model, Service & Repository (`A Biblioteca`)**: Toda a lógica de negócio (`Service`), acesso a dados (`Repository`) e modelos (`Model` com SQLModel) é fornecida pela biblioteca **`HEROLIBsaraivagustavo`**.

### ✨ Uso de Generics
A biblioteca `HEROLIBsaraivagustavo` faz uso intensivo de **Generics** do Python (`TypeVar`). Isso permite que as classes `Repository` e `Service` operem com qualquer modelo (`Hero` ou `Team`) sem reescrever código repetitivo.

---

### 💾 Banco de Dados
Conforme definido pela biblioteca, a API utiliza um banco de dados **SQLite**. Isso garante que a aplicação seja leve, autônoma e fácil de executar.

---

### 🚀 Funcionalidades
* ✅ **Heróis**: CRUD completo para o cadastro de heróis.
* ✅ **Times**: CRUD completo para os times, aos quais os heróis podem ser vinculados.
* ✅ **Documentação Automática**: Interface interativa em `/docs` e `/redoc`.
"""

app = FastAPI(
    title="API de Heróis e Times",
    description=descricao,
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
