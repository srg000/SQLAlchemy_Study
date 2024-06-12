from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

# engine = create_engine("mysql://root:root@127.0.0.1:3306/testdb", echo=True)
engine = create_engine(
    "sqlite:///./sqlalchemy_basic.db", echo=True, connect_args={"check_same_thread": False}
)
meta_data = MetaData()

# 将表结构已经放入了meta_data
department_table = Table(
    "department", meta_data,
    Column("id", Integer, primary_key=True, comment='部门id'),
    Column("name", String, unique=True, nullable=False, comment="部门名称"),
)

employee_table = Table(
    "employee", meta_data,
    Column("id", Integer, primary_key=True, comment='员工id'),
    Column("name", String(255), unique=True, nullable=False, comment="员工姓名"),
    Column("birthday", String, nullable=True, comment="员工生日"),
    Column("department_id", Integer, ForeignKey("department.id"), nullable=False, comment="员工所属部门id"),
)

meta_data.create_all(engine)