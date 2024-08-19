import httpx
from fastapi.exceptions import HTTPException
from fastapi import Header, Depends
from typing import Annotated


def get_authenticated(Authorization: str = Header(...)):
    with httpx.Client(timeout=2) as client:
        headers = {
            "Authorization": Authorization
        }
        req = client.get(url="http://localhost:8000/authenticate", headers=headers)
    
    if req.status_code == 401:
        raise HTTPException(status_code=401, detail=req.json().get("message"))
    
    return True

authentication = Annotated[bool, Depends(get_authenticated)]