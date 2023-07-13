import os
from fastapi import FastAPI

app = FastAPI()

bind_address = os.getenv('BIND', '0.0.0.0')


# an9atbr9.up.railway.app
@app.get("/")
async def root():
    return {"message": "EngeSEP API"}


@app.get("/autentic/{user}/{password}")
async def say_hello(name: str, password: str):
    if password == "123":
        return {"message": f"Hello {name}"}
    return {"message": "Password incorrecto"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")

