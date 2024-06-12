from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from typing_extensions import Annotated

engine = create_engine(
    "sqlite:///./sqlalchemy_orm_new_mapping.db", echo=True, connect_args={"check_same_thread": False}
)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

'''
Mapped映射字段 
mapped_column指定更多定义信息
Annotated 来定义模板字段信息
'''
int_pk = Annotated[int, mapped_column(Integer, primary_key=True, comment='主键ID')]
required_name = Annotated[str, mapped_column(String, unique=True, index=True)]

class Person(Base):
    __tablename__ = "person"

    id: Mapped[int_pk]
    name: Mapped[required_name]
    address: Mapped[str] = mapped_column(String(255), default="lalala", nullable=True)
    create_datetime: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')
    update_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='更新时间'
    )


Base.metadata.create_all(bind=engine)