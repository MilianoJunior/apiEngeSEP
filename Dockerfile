# Use uma imagem oficial do Python
FROM python:3.8-slim

# Diretório de trabalho no container
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Declare variáveis de ambiente Railway como ARG para que elas possam ser passadas no momento da construção
ARG RAILWAY_ENVIRONMENT
ENV RAILWAY_ENVIRONMENT=$RAILWAY_ENVIRONMENT

# Comando para executar a aplicação usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
