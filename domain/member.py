from sqlalchemy import Column, Integer, String

from config.database import Base


class Member(Base):
    __tablename__ = "member_entity"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
