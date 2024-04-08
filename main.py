from fastapi import FastAPI
import laftel

app = FastAPI()


@app.get("/{id}")
async def root(id: int):
    a = await laftel_get(id)
    return a


async def laftel_get(id: int):
    anime = await laftel.getAnimeInfo(id)

    return anime.__dict__
