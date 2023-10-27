# Clean FastAPI studies

Bem vindo ao meu repo de estudos de arquitetura utilizando o FastAPI

## Padrões de Arquitetura

### MVC

O padrão de arquitetura MVC, assim como o conceito de camadas, é antigo, sendo apresentado pela primeira vez no fim da década de 70. Mas foi sua aplicabilidade em soluções web que o tornou popular e um padrão bastante adotado por frameworks em diversas linguagens.
Esse é um dos padrões mais utilizados nas aplicações em Python, pois é o similar ao adotado pelo Django - [Django MVT](https://docs.djangoproject.com/en/4.2/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names).

Em uma visão resumida, esse padrão determina a organização do software em 3 camadas, sendo elas:

Model: camada de manipulação dos dados.
View: camada de interação do usuário.
Controller: camada de controle entre Model e View.

O MVC se tornou um dos padrões mais conhecidos e associados ao uso de 3 camadas, ao ponto de ser confundido por muitos com o próprio conceito de 3 camadas. Ele propõe que a camada Model seja responsável pela leitura e escrita de dados, View pela interação com o usuário e Controller seja a responsável por receber as requisições da View, interagir com a Model e retornar os dados para View.

## Clean Arch, DDD e Hexagonal

**Clean Architecture** aborda vários conceitos importantes para implementar software e camadas organizadas e reutilizáveis, como as camadas mais próximas do núcleo definirem as interfaces para persistência e a implementação concreta destas interfaces estar no círculo mais externo fazendo parte de “Frameworks e Drivers”, o que é a inversão de dependências na prática, podendo inclusive também fazer uso de injeção de dependência.

Além disto trabalha sobre a representação de casos de uso, trazendo para o código uma representação mais forte dos casos de uso dos usuários do software, o que acompanha também questões abordadas em DDD.

Este padrão é um amadurecimento com relação ao uso de camadas, e requer desenvolvedores(as) com conhecimento e maturidade nestes temas, além de alguns padrões de projeto. É uma das arquiteturas que proporcionam maior organização das responsabilidades do código sendo fortemente recomendada pelo guia.

**DDD** é uma sigla para Domain Driven Developmento, onde o objetivo principal é estruturar e modelar a implementação do código com foco no domínio do negócio. É uma abordagem que explicitou à desenvolvedores(as) que há uma diferença entre código de infraestrutura do software, de controle da aplicação e de interação do usuário para código focado na lógica e regras de negócio.

Essa abordagem, caminha na direção da visão de camadas, principalmente com relação a camada de negócio. Porém ela é mais profunda, apontando que:

Algumas camadas lógicas dentro da camada de negócio como Controllers, ou outras relacionadas ao fluxo da aplicação não fazem parte do domínio de negócio.
Artefatos relacionados ao domínio devem ser agrupados por contextos e não por suas camadas lógicas.

Na visão de DDD, a camada de domínio é o ativo de maior valor e importância em um software, sendo ela a camada a ter a maior chance de reutilização. Outras camadas de um software também podem fazer uso de boas práticas do DDD, como a organização por contextos, uso da linguagem ubíqua, dentre outros.

DDD explora outros aspectos e conceitos e neste tópico o guia apenas exemplifica como a arquitetura de camadas e DDD convergem, sendo uma ótima abordagem a ser aplicada no desenvolvimento de software.

**Hexagonal Architecture** é um padrão apoiado sobre o uso de camadas, e que busca uma outra forma de representar e aplicar na prática as questões de organização, isolamento e dependência entre as camadas. Quando criado, teve como motivação os problemas citados no tema Camadas com relação a desorganização no uso de camadas e a infiltração de lógica de negócio em outras camadas.

A proposta é que o software seja implementado sem se preocupar com uma interface para o usuário ou banco de dados. O que remete o foco ao domínio do negócio. Há uma mudança com relação à visão tradicional de camadas, abandonando a visão vertical e trazendo uma visão hexagonal onde cada lado do hexágono representa uma integração, que pode ser vista como outras camadas.

-----

### Preparando o ambiente

#### Iniciando o virtual environment

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

#### Iniciando a App

```shell
uvicorn src.app:main --reload
```

ou pelo Makefile

```
make local
```

Quando a aplicação for iniciada, será possível acessar pelo navegador web o localhost na porta 3000, dessa forma:

`localhost:3000`

### Branch 1-start-app

Nessa branch está a primeira versão da aplicação.

Uma aplicação em um único script Python `src/main.py`
Que contém a inicialização da aplicação, todos as rotas definidas até o momento e uma solução fake para persistencia dos dados.

Também há os testes automatizados referentes a as rotas criadas.
Repare que no arquivo `tests/__init__.py` utilizedi uma solução para permitir o import dos arquivos necessários para executar os casos de testes.

Para executar os testes:

```shell
pytest
```

ou utilize o Makefile

```shell
make tests
```

#### Testes Unitários e de Integração

Esses testes automatizados são a garantia que nossa aplicacão está funcionando e que durante a evolução dela não iremos "quebrar" nada ou que possamos voltar para orignal de funcionamento.

- Detecção Precoce de Erros: Os testes unitários identificam problemas de lógica, erros de programação e regressões no início do ciclo de desenvolvimento, facilitando correções imediatas.
- Melhoria da Qualidade do Código: Testes unitários incentivam a criação de código mais modular e de alta qualidade, pois você precisa projetar seu código de uma maneira que seja facilmente testável.
- Documentação Executável: Os testes unitários funcionam como documentação executável, descrevendo como as partes do código devem se comportar. Isso torna o código mais claro e legível.
- Facilitação da Refatoração: Quando você precisa fazer alterações no código, os testes unitários atuam como uma rede de segurança, permitindo que você faça alterações com confiança, sabendo que os testes verificarão se nada quebrou.
- Aceleração do Desenvolvimento: À medida que a base de código cresce, os testes unitários economizam tempo a longo prazo, pois ajudam a evitar a introdução de novos bugs à medida que você adiciona funcionalidades.

Nessa primeira branch, não há um padrão de arquitetura claramente definido. Temos diversas responsabilidades misturadas, mas é um ponto de partida.

### Branch 2-fastapi-stuff

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

- [FastAPI - Body Fields](https://fastapi.tiangolo.com/tutorial/body-fields/)
- [Pydantic - BaseModel](https://docs.pydantic.dev/latest/concepts/models/)

A validação de input utilizando as propriedades do Pydantic é um universo a parte e muito prático no dia a dia. Sugiro que estude conforme necessidades que a sua aplicação apresente.

### Continuous Development

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

```shell
make build
make compose
make down
make stop
```

Esses comandos serão utilizados para construir a aplicação num container isolado, construir todo o ambiente do projeto, inclusive os demais componentes com o docker-compose. Desmontar a aplicação e parar os containers e componentes em execução.

### Feature/dto

Para manter a separação de responsabilidades, nessa branch as rotas ou endpoints foram removidos do arquivo principal `src/main.py` e foram remanejadas parauma nova pasta `controller`. Aproveitando os recurosos do FastAPI, foram nomeadas conforme convenção (`v1`).
O DTO (data transfer object) também foi deslocado para uma pasta inferior dentro do controller/item, assim facilita a edição desse objeto.

### Database

Muita evolução em relação a branch anterior.

Primeiro será necessário disponibilizar um banco de dados local, algumas soluções:

#### Banco de dados Local

#### Postgres local com docker

```shell
docker run --name postgresserver -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=app -d postgres
```

#### Aplicação local com docker-compose

```shell
make build
make compose
```

### criar tabelas

```shell
docker exec -it postgresserver bash
psql -h localhost -U postgres
CREATE DATABASE app; -> não esquecer do ;
\q
exit
```

### Instalando o Postgres

Consulte o site oficial: [PostregreSQL](https://www.postgresql.org/) para ver os passos de instalação.

### Evolução na Branch

#### Makefile e docker-compose

O Makefile foi atualizado para realizar o deploy, stop e remoção do Postgres local via Docker.
Foi incluído também um novo comando para limpar os arquivos de cache, reports de testes e demais arquivos que são criados durante a execução da aplicação.

#### Arquivo .env

Em uma aplicação, é uma boa prática definir variáveis em função do local onde a aplicação está sendo executada, por exemplo, um ambiente local, um ambiente remoto, de desenvolvimento ou produção.O valor de cada variável é utilizada pela aplicação para alterar a configuração conforme o local em que está sendo executada.

As variáveis utilizadas pelo projeto, ficam no arquivo .env, na raiz do projeto.  Uma das variáveis é o endereço do banco de dados.

#### Evoluindo o Design da Aplicação

##### Camada de aplicação

Os **Usecases** ou casos de uso, são os processos que a serem acionados no centro de aplicação por uma ou várias interfaces de externas a aplicação.
Por exemplo, em um CMS, poderíamos ter a interface do usuário do aplicativo real usada pelos usuários comuns, outra interface do usuário independente para os administradores do CMS, outra interface do usuário da CLI e uma API da Web. Essas UIs (aplicativos) podem desencadear casos de uso que podem ser específicos para um deles ou reutilizados por vários deles.

Os usecases são definidos na camada de aplicação, o centro ou a primeira camada fornecida pelo DDD e usada pela arquitetura .

###### Camada de Domínio

Mais para dentro das camadas, temos a Camada de Domínio. Os objetos desta camada contêm os dados e a lógica para manipular esses dados, que são específicos do próprio Domínio e são independentes dos processos de negócio que acionam essa lógica, são independentes e completamente inconscientes da Camada de Aplicação.

No entanto, por vezes encontramos alguma lógica de domínio que envolve entidades diferentes, do mesmo tipo ou não, e sentimos que essa lógica de domínio não pertence às próprias entidades, sentimos que essa lógica não é da sua responsabilidade direta.
Portanto, nossa primeira reação poderia ser colocar essa lógica fora das entidades, em um Serviço de Aplicação. No entanto, isso significa que essa lógica de domínio não será reutilizável em outros casos de uso: a lógica de domínio deve ficar fora da camada de aplicação!
A solução é criar um Serviço de Domínio, que tem a função de receber um conjunto de entidades e realizar sobre elas alguma lógica de negócio. Um Serviço de Domínio pertence à Camada de Domínio e, portanto, não sabe nada sobre as classes da Camada de Aplicação, como os Serviços de Aplicação ou os Repositórios. Por outro lado, pode utilizar outros Serviços de Domínio e, claro, os objetos do Modelo de Domínio.

O isolamento da camada de domínio, facilita a execução de testes unitários, de forma a testar as regras de negócio de forma isolada. Veja os exemplos em `/tests/unit`.

###### Desacoplando os componentes

Assim como as unidades de código menores (classes, interfaces, características, mixins,…), como o exemplo da camada de domínio, também as unidades de código de maiores (componentes) se beneficiam de baixo acoplamento e alta coesão.

Para desacoplar classes usamos Injeção de Dependência, injetando dependências em uma classe em vez de instanciá-las dentro da classe.

###### O que é a "Injeção de Dependências"

"Injeção de dependências" significa, em programação, que existe uma forma de o seu código (neste caso, as suas funções de operação de caminhos) declarar coisas de que necessita para funcionar e utilizar: "dependências".

Depois, esse sistema (neste caso, a FastAPI) encarregar-se-á de fazer o que for necessário para fornecer ao seu código essas dependências necessárias ("injetar" as dependências).

Isto é muito útil quando é necessário:

- Ter lógica partilhada (a mesma lógica de código repetidamente).
- Partilhar ligações a bases de dados.
- Aplicar segurança, autenticação, requisitos de função, etc.
- E muitas outras coisas...
- Tudo isto, minimizando a repetição de código.

O FastAPI favorece a injeção dependência, veja o exemplo no `src/controller/v1/item_controller.py`:

```python

# Rota de criação de itens
@item_router.post("/items/")
async def create_item(item: ItemSchema, use_case: CreateItemUsecase = Depends(CreateItemUsecase)) -> ItemSchema:
    item = await use_case.execute(item)
    return item
```

a classe `Depends`, faz todo o trabalho de injeção para nós.

###### Camada de Drivers and Adapters

Na camada mais externa, temos as classes de bibliotecas, frameworks e quaisquer sistemas externos. Por exemplo, é nessa camada que ficam os sistemas responsáveis por persistência em bancos de dados, construção de interfaces com usuários, envio de mails, comunicação com provedores de pagamento, comunicação com determinados hardware, etc.

No exemplo, usamos um serviço de terceiros, o Postgres para persistencia dos dados, toda a comunicação e interface com esse serviço fica isolado na camada de frameworks. Tais classes ficam na camada mais externa de uma Arquitetura Limpa.

#### Testes

Os testes criados inicialmente, garantiram que  a aplicação continuar funcionando corretamente. Foram necessários alguns ajustes, pois como houveram mudanças na estrutura do código, os testes precisarm refletir tais mudanças.

Destaco que com o isolamento das camadas de domínio, ficou mais simples a execução de testes unitários aplicando diretamente as regras de negócio.

Atenção: Mesmo com testes de integração ou end to end, sem realizar mocks do banco de dados, ou seja, utilizando todos os recursos da aplicação, inclusive um banco de dados em disponível para execução dos testes, foi necessário alterar a cobertura de testes do projeto, pois o framework escolhido utiliza uma API de multiprocessamento para execução do flux assíncrono, enquanto o framework de banco de dados utiliza outra API de multiprocessamento.

É possível ver que esse assunto está em discussões no [GitHub]((https://github.com/nedbat/coveragepy/issues/1082))
