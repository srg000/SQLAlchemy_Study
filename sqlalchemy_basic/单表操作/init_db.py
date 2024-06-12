from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

# engine = create_engine("mysql://root:root@127.0.0.1:3306/testdb", echo=True)
engine = create_engine(
    "sqlite:///./sqlalchemy_basic.db", echo=True, connect_args={"check_same_thread": False}
)
meta_data = MetaData()

# 将表结构已经放入了meta_data
person = Table(
    "person", meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True, nullable=False),
    Column("birthday", String, nullable=False),
    Column("address", String(255), nullable=True)
)