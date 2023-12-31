import os
from fastapi import FastAPI
from libs.connection import DatabaseManager

app = FastAPI()

bind_address = os.getenv('BIND', '0.0.0.0')
port = int(os.getenv("PORT", default=8000))

print(f"Starting server on {bind_address}")
print(f"PORT: {port}")
# an9atbr9.up.railway.app
@app.get("/")
async def root():
    dados = {
        "nome": "EngeSEP",
        "versao": "1.0.1",
        "descricao": "API para aquisição de dados de sensores",
        "autor": "EngeSEP",
        "email": "engesep@engesep.com.br",
        "telefone": "(11) 99999-9999",
        "endereco": "R. Dom Pedro I, 969 - São Cristóvão, Chapecó - SC, 89803-220",
        "licenca": "MIT",
        "atualizado": "22/08/2023 17:58:00",
        "servidor": "an9atbr9.up.railway.app",
        "site": "https://engesep.com.br",
        "documentacao": "https://engesep.com.br/docs",
        "repositorio": "https://github.com/MilianoJunior/apiEngeSEP",
    }
    return dados

@app.post("/consulta_id/")
async def consulta_id(id: int):
    db = DatabaseManager(table='cgh_fae')
    leitura = db.where_id(id)
    return leitura.to_json()

@app.post("/consulta_condicao/")
async def consulta_condicao(condicao: str):
    db = DatabaseManager(table='cgh_fae')
    leitura = db.where_condition(condicao)
    return leitura.to_json()


@app.get("/autentic/{user}/{password}")
async def say_hello(name: str, password: str):
    if password == "123":
        return {"message": f"Hello {name}"}
    return {"message": "Password incorrecto"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=bind_address, port=port, log_level="info")


'''
177.38.15.73
'''