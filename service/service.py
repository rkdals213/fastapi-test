from sqlalchemy.orm import Session

from repository.repository import MemberRepository


class MemberService:
    def __init__(self, db: Session):
        self.db = db

    def create_member(self) -> int:
        member = MemberRepository(self.db).create_member()

        return member.id

    def find_member(self) -> dict[str, str | int]:
        member = MemberRepository(self.db).find_member(1)
        return {"id": member.id, "email": member.email, "name": member.name}
