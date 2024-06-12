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
    Column("birthday", String, nullable=False)
)
# 通过engine引擎执行并创建meta_data中所有的表
meta_data.create_all(engine)

# insert one record
# person_insert_sql = person.insert().values(name="srg", birthday="2000-11-05")
# with engine.connect() as conn:
#     res = conn.execute(person_insert_sql)
#     print(res.inserted_primary_key)
#     conn.commit()

# insert multiple records
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert, [
        {"name": "Jack", "birthday": "2000-10-13"},
        {"name": "Mary", "birthday": "2000-10-14"},
        {"name": "Smith", "birthday": "2000-10-15"},
    ])
    conn.commit()