from fastapi import FastAPI

from routers import subModule1, subModule2

app = FastAPI()
app.include_router(subModule1.router)
app.include_router(subModule2.router)


@app.get("/")
async def root():
    return {"message": "Hello World",
            "message2": "message2"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
