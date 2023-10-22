# Use a imagem base do Python
FROM python:3.10.12-slim

# Define o diretório de trabalho na imagem
WORKDIR /app

# Preparando o ambiente
RUN python -m pip install --upgrade pip
# Instale as dependências do aplicativo
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copie os arquivos necessários para a imagem
COPY src /app/src


# Exponha a porta em que a aplicação FastAPI será executada
EXPOSE 8000

# Crie um usuário não privilegiado
RUN useradd -ms /bin/bash appuser

# Defina o usuário como o usuário padrão
USER appuser

# Comando para executar a aplicação com o Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
