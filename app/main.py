from fastapi import FastAPI

from .router import adventure, user

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"status": "ok"}


app.include_router(user.router)
app.include_router(adventure.router)
