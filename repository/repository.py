from sqlalchemy.orm import Session

from domain import member
from domain.member import Member


class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_member(self) -> Member:
        db_member = member.Member(
            email="rkdals213@naver.com",
            name="Kang"
        )
        self.db.add(db_member)
        self.db.commit()
        self.db.refresh(db_member)

        return db_member

    def find_member(self, member_id: int) -> Member | None:
        return self.db.query(member.Member).filter(member.Member.id == member_id).first()
