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


## Branch 2-fastapi-stuff

O FastAPI foi o framework escolhido devido a diversas facilidades.
Como o próprio autor diz: "Apoiado nos ombros de gigantes"

Nessa branch alterei as funções de rotas para utilizar o processamento assíncrono e adicionei uma nova classe ao `src/main.py`, a classe Item.

Essa nova classe herda a propriedades do `BaseModel`, uma classe base do Pydantic, facilitando a criação de documentações interativas, veja um exemplo prático, inicializando a aplicação com:

```shell
make run
```

ou simplesmente
```shel
uvicorn src/main.py --reload
```

a partir do navegador web, acesse: `http://127.0.0.1:8000/docs`. Agora podemos interagir com o backend, preparando as requests. 

Observe também, que foram criados dois novos testes, com body inválidos. Essa é outra vantagem de utilizar o Pydantic, automaticamente é criado um json schema e a cada request o body é validado contra esse schema.
Veja mais em:
[FastAPI - Body Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
[Pydantic - BaseModel](https://docs.pydantic.dev/latest/concepts/models/)

A validação de input utilizando as propriedades do Pydantic é um universo a parte e muito prático no dia a dia. Sugiro que estude conforme necessidades que a sua aplicação apresente.