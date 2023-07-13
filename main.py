import os
from fastapi import FastAPI

app = FastAPI()

bind_address = os.getenv('BIND', '0.0.0.0')

print(f"Starting server on {bind_address}")
# an9atbr9.up.railway.app
@app.get("/")
async def root():
    dados = {
        "nome": "EngeSEP",
        "versao": "1.0.0",
        "descricao": "API para aquisição de dados de sensores",
        "autor": "EngeSEP",
        "email": "engesep@engesep.com.br",
        "telefone": "(11) 99999-9999",
        "endereco": "R. Dom Pedro I, 969 - São Cristóvão, Chapecó - SC, 89803-220",
        "licenca": "MIT",
        "atualizado": "13/07/2023 19:15:00",
        "servidor": "an9atbr9.up.railway.app",
        "site": "https://engesep.com.br",
        "documentacao": "https://engesep.com.br/docs",
        "repositorio": "https://github.com/MilianoJunior/apiEngeSEP",
    }
    return dados


@app.get("/autentic/{user}/{password}")
async def say_hello(name: str, password: str):
    if password == "123":
        return {"message": f"Hello {name}"}
    return {"message": "Password incorrecto"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", default=5000)), log_level="info")

