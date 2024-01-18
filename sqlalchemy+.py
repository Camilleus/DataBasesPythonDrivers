from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

uri = "sqlite:///superblog"
engine = create_engine(uri)

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)


Base.metadata.create_all()