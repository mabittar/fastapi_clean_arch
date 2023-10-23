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


## Continuous Development

Da mesma forma que empresas de logística usam contêineres físicos para isolar diferentes cargas para transporte em navios e trens, as tecnologias de desenvolvimento de software cada vez mais usam um conceito chamado de conteinerização.

Um container é:
- Um caixa invisível em torno do código que foi criado e suas dependências;
- Possui acesso limitado a sua própria partição do file system e hardware;
- Apenas necessita de algumas chamadas de sistema para serem criados e iniciados, o mais rápido possível;
- Apenas precisam do Kernel do Sistema Operacional que suporte container e o runtime do container
- Escala como PaaS, mas possui a mesma flexibilidade de um IaaS.

Isso faz o código ser ultra portátil, pois o hardware e o sistema operacional podem ser tratados como uma caixa preta (black box)

Um container nada mais é do que um software usado para empacotar e isolar virtualmente aplicativos e suas dependências para permitir maior escalabilidade, disponibilidade e portabilidade em diversos ambientes de computação, incluindo sistemas _bare-metal/machine_, em nuvem, máquinas virtuais (VMs) e alguns sistemas operacionais.

Os containers são executados em ambientes virtuais, geralmente como parte de um sistema de computação em nuvem.

Porém em alguns casos, um único arquivo Docker não é suficiente. Adiante iremos adicionar outros componentes complexo à ao projeto, como um banco de dados. Você pode tentar adicioná-lo diretamente ao Dockerfile ou adicioná-lo por meio de um contêiner adicional. Felizmente, o docker-compose oferece suporte a configurações de vários contêineres gerenciados.

Foram adicionados alguns novos comandos ao arquivo Makefile

```
make build 
make compose
make down
make stop
```

Esses comandos serão utilizados para construir a aplicação num container isolado, construir todo o ambiente do projeto, inclusive os demais componentes com o docker-compose. Desmontar a aplicação e parar os containers e componentes em execução.


## Feature/dto

Para manter a separação de responsabilidades, nessa branch as rotas ou endpoints foram removidos do arquivo principal `src/main.py` e foram remanejadas parauma nova pasta `controller`. Aproveitando os recurosos do FastAPI, foram nomeadas conforme convenção (`v1`).
O DTO (data transfer object) também foi deslocado para uma pasta inferior dentro do controller/item, assim facilita a edição desse objeto.