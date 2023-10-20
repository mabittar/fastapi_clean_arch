# Clean FastAPI studies

Welcome to my FastAPI studies repo


## Start env

```shell
python -m venv .venv
source .venv/bin/activate
pip install requirements.txt
pre-commit install
pre-commit run
```

or just use Makefile. Before use it, confirm installtion

```shell
make setup
```


## Start App

```shell
uvicorn src.app:main --reload
```