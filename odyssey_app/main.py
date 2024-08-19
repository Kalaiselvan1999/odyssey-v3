from fastapi import FastAPI, Request, Depends
from dependencies import authentication

app = FastAPI()


@app.middleware('http')
async def sys(request: Request, call_next):
    response = await call_next(request)
    return response


@app.get('/ping')
async def pong():
    return "pong"


@app.get('/odyssey/{odyssey_id}')
async def get_odyssey(odyssey_id: int, token: authentication):
    try:
        return {
            "name": "Odyssey",
            "from": "2024-08-31",
            "to": "2024-12-31"
        }
    except Exception as e:
        return {"detail": str(e)}
