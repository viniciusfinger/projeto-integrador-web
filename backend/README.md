# Backend do Projeto

Este é o backend do projeto, desenvolvido com FastAPI.

## Requisitos

- Python 3.11 ou superior

## Configuração do Ambiente

1. Crie um ambiente virtual (venv):
```bash
python -m venv env
```

2. Ative o ambiente virtual:

No Windows:
```bash
.\env\Scripts\activate
```

No macOS/Linux:
```bash
source env/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado

2. Execute o servidor:
```bash
uvicorn main:app --reload
```

O servidor estará disponível em `http://localhost:8000`
