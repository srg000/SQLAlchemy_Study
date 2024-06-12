from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:///./sqlalchemy_basic_orm.db", echo=True, connect_args={"check_same_thread": False}
)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# 将表结构已经放入了meta_data
class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    address = Column(String(255), nullable=True)


Base.metadata.create_all(bind=engine)