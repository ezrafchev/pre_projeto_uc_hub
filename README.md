
# Projeto UC HUB

## Descrição do Projeto
Este projeto é um sistema de controle de estoque para uma clínica médica. Ele permite o registro de insumos, controle de estoque e avaliação de tratamentos que mais demandam insumos.

## Pré-requisitos
- Python 3.8 ou superior
- FastAPI
- SQLite
- Navegador Web

## Instruções de Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/ezrafchev/pre_projeto_uc_hub.git
    cd pre_projeto_uc_hub
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar o Projeto
1. Inicie o servidor FastAPI:
    ```bash
    uvicorn backend.main:app --reload
    ```

2. Abra o navegador e acesse `http://127.0.0.1:8000`.

## Estrutura do Projeto
```
pre_projeto_uc_hub/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── stock.html
│   └── evaluation.html
├── db/
│   └── database.db
├── venv/
└── requirements.txt
```

## Endpoints da API

### `POST /insumos/`
Cria um novo insumo.

**Request:**
```json
{
  "nome": "Insumo A",
  "quantidade": 10,
  "preco": 5.99
}
```

**Response:**
```json
{
  "id": 1,
  "nome": "Insumo A",
  "quantidade": 10,
  "preco": 5.99
}
```

### `GET /insumos/`
Retorna uma lista de insumos.

**Response:**
```json
[
  {
    "id": 1,
    "nome": "Insumo A",
    "quantidade": 10,
    "preco": 5.99
  }
]
```

### `GET /insumos/{insumo_id}`
Retorna um insumo específico.

**Response:**
```json
{
  "id": 1,
  "nome": "Insumo A",
  "quantidade": 10,
  "preco": 5.99
}
```

## Exemplos de Uso

### Criar um novo insumo
```bash
curl -X POST "http://127.0.0.1:8000/insumos/" -H "Content-Type: application/json" -d '{"nome": "Insumo A", "quantidade": 10, "preco": 5.99}'
```

### Listar insumos
```bash
curl -X GET "http://127.0.0.1:8000/insumos/"
```

### Obter um insumo específico
```bash
curl -X GET "http://127.0.0.1:8000/insumos/1"
```
