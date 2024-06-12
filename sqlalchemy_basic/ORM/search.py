from init_db import sessionLocal, Person

with sessionLocal() as db:
    # 查询全部
    # res = db.query(Person).all()

    # 条件查询
    # 注意：只写 db.query(Person).filter(Person.address == 'test')，只拿到了查询语句，具体查询要使用one(), first(), scalar()
    res_condition = db.query(Person).filter(Person.address == 'test').one()
    print(res_condition.name)

    # 查询一条数据
    # one(), first(), scalar()