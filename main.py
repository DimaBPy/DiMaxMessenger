from fastapi import FastAPI

app = FastAPI(title='DiMax', version='0.0.1')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
