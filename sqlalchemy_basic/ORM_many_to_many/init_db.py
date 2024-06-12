from datetime import datetime
from typing import List

from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated

engine = create_engine(
    "sqlite:///./orm_many_to_many.db", echo=True, connect_args={"check_same_thread": False}
)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

int_pk = Annotated[int, mapped_column(Integer, primary_key=True, comment='主键ID')]
required_name = Annotated[str, mapped_column(String, unique=True, index=True)]


# 多对多的关联表
association_table = Table(
    "user_role", Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("role.id"), primary_key=True)
)


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int_pk]
    name: Mapped[required_name]
    create_datetime: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')
    update_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='更新时间'
    )

    # 重写打印方法
    def __repr__(self):
        return f'id:{self.id}, name:{self.name}'


class User(Base):
    __tablename__ = "user"

    id: Mapped[int_pk]
    name: Mapped[required_name]
    password: Mapped[str] = mapped_column(String(125), nullable=False, comment="密码")
    create_datetime: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')
    update_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='更新时间'
    )

    roles: Mapped[List["Role"]] = relationship(secondary=association_table, lazy=False)

    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, password:{self.password}'


Base.metadata.create_all(bind=engine)