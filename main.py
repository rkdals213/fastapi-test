from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from service.service import MemberService

app = FastAPI()


@app.post("/create_member")
async def create_member_route(db: Session = Depends(get_db)):
    return MemberService(db).create_member()


@app.post("/find_member")
async def find_member(db: Session = Depends(get_db)):
    return MemberService(db).find_member()
