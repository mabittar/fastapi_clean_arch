# Clean FastAPI studies

Welcome to my FastAPI studies repo

## Preparando o ambiente

### Iniciando o virtual environment 
O Virtual environment serve para isolar sua aplicação das outras dependências do sistema. Assim as bibliotecas necessárias ou libs não interferem com a versão global do sistema.

```shell
python -m venv .venv
source .venv/bin/activate
pip install requirements.txt
pre-commit install
pre-commit run
```

Ou utilize o Makefile. Antes de utilizar esse recursos verifique se o make está disponível para ser chamado na shell
```shell
make setup
```


### Iniciando a App

```shell
uvicorn src.app:main --reload
```

ou pelo Makefile

```
make local
```

Quando a aplicação for iniciada, será possível acessar pelo navegador web o localhost na porta 3000, dessa forma:

`localhost:3000`

## Branch 1-start-app

Nessa branch está a primeira versão da aplicação. 

Uma aplicação em um único script Python `src/main.py`
Que contém a inicialização da aplicação, todos as rotas definidas até o momento e uma solução fak para persistencia dos dados.

Também há os testes automatizados referentes a as rotas criadas.
Repare que no arquivo `tests/__init__.py` utilizedi uma solução para permitir o import dos arquivos necessários para executar os casos de testes.

Para executar os testes:

```
pytest
```

ou utilize o Makefile

```
make tests
```

Esses testes automatizados são a garantia que nossa aplicacão está funcionando e que durante a evolução dela não iremos "quebrar" nada ou que possamos voltar para orignal de funcionamento.
