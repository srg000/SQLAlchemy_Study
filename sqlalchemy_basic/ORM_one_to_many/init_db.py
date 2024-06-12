from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
from typing_extensions import Annotated

engine = create_engine(
    "sqlite:///./orm_one_to_many.db", echo=True, connect_args={"check_same_thread": False}
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


class Department(Base):
    __tablename__ = "department"

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
        return f'id:{self.id}, name:{self.name}, create_datetime:{self.create_datetime}'


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int_pk]
    name: Mapped[required_name]
    create_datetime: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='创建时间')
    update_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        comment='更新时间'
    )

    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("department.id"))
    # lazy=False时，当查询Employee时，会联表查询到Department中的所有字段信息，True时，只在调用employee.department时才查询
    # 当指明backref="employees"时，我们在调用 department对象时，系统会动态给它分配一个employees字段（在实际项目中，这个字段时不加的，浪费性能）
    # back_populates是双向指定，在实际项目中，这个字段时不加的，浪费性能
    department: Mapped[Department] = relationship(foreign_keys=department_id, lazy=False, backref="employees")

    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, create_datetime:{self.create_datetime}'


Base.metadata.create_all(bind=engine)