# Use uma imagem oficial do Python
FROM python:3.8-slim

# Diretório de trabalho no container
WORKDIR /app

# Instale dependências necessárias para compilar o mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libmysqlclient-dev pkg-config

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Declare variáveis de ambiente Railway como ARG para que elas possam ser passadas no momento da construção
ARG RAILWAY_ENVIRONMENT
ENV RAILWAY_ENVIRONMENT=$RAILWAY_ENVIRONMENT

# Comando para executar a aplicação usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
