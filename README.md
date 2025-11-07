# API de Gerenciamento de Heróis

Esta é uma API RESTful construída com **FastAPI** para gerenciar Heróis e Times.

O principal objetivo deste projeto é demonstrar uma arquitetura de API limpa, seguindo o padrão de "Controllers" (com `APIRouter`) que consome uma biblioteca de lógica de negócios externa: a [HEROLIBsaraivagustavo](https://pypi.org/project/HEROLIBsaraivagustavo/).

## ✨ Recursos

* **API Rápida:** Construída com [FastAPI](https://fastapi.tiangolo.com/), oferecendo alto desempenho e documentação automática.
* **Arquitetura MVC/Router:** O código é organizado em "Controllers" (Rotas) para `heroes` e `teams`, mantendo o `main.py` limpo e focado na configuração.
* **Documentação Automática:** Acesso instantâneo à documentação interativa (Swagger UI) em `/docs`.
* **Lógica de Negócios Abstraída:** Toda a interação com o banco de dados (CRUD, modelos, sessões) é gerenciada pela biblioteca `HEROLIBsaraivagustavo`.

## 🚀 Dependência Principal: `HEROLIBsaraivagustavo`

Esta API não contém lógica de banco de dados diretamente. Ela atua como a camada de "Controller" e delega todas as operações de dados para a biblioteca `HEROLIBsaraivagustavo`.

* **Biblioteca:** `HEROLIBsaraivagustavo`
* **Descrição da Lib:** "Biblioteca para gerenciamento de heróis e seus times, utilizando banco de dados em memória com SQLModel."
* **Camadas da Lib:** A biblioteca já fornece as camadas de `Service` e `Repository` que esta API utiliza.

## 📦 Instalação

1.  Clone este repositório (ou crie a pasta do projeto).
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate # Windows
    source .venv/bin/activate # Linux ou MacOS
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Como Executar

Com o ambiente virtual ativado, execute o servidor Uvicorn a partir do diretório raiz do projeto:

```bash
uvicorn main:app --reload
O servidor estará disponível em http://127.0.0.1:8000.
```

## 📚 Endpoints da API
Acesse a documentação interativa gerada automaticamente pelo FastAPI para ver, testar e interagir com todos os endpoints disponíveis:

```bash
No navegador, ao final do servidor adicione "docs". 
http://127.0.0.1:8000/docs.
```

Os endpoints estão organizados em duas seções principais:

- /heroes: Endpoints para Criar, Ler, Atualizar e Deletar Heróis.

- /teams: Endpoints para Criar e Ler Times.

## ⚖️ Licença
Este projeto está licenciado sob os termos da Licença MIT.