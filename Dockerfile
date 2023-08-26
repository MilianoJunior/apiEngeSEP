# Use a imagem base do Python
FROM python:3.8

# Diretório de trabalho no container
WORKDIR /app

# Instale dependências necessárias para compilar o mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Declare variáveis de ambiente Railway como ARG para que elas possam ser passadas no momento da construção
ARG RAILWAY_ENVIRONMENT
ENV RAILWAY_ENVIRONMENT=$RAILWAY_ENVIRONMENT

# Instale as dependências do Python
RUN python -m venv /opt/venv && . /opt/venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Comando para executar a aplicação usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
