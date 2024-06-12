from sqlalchemy.sql.elements import and_, or_

from init_db import engine, person as person_table

with engine.connect() as conn:

    '''
    普通查询
    '''
    # query_sql = person_table.select()
    # result_set = conn.execute(query_sql)
    # # 查询全部的数据
    # result_all = result_set.fetchall()
    # # 查询第一个数据
    # result_first = result_set.first()

    '''
    条件查询
    '''
    query_and = person_table.select().where(
        person_table.c.name == "srg", person_table.c.id >= 1
    )
    query_or = person_table.select().where(
        or_(
            person_table.c.name == "srg",
            and_(
                person_table.c.birthday == "2000-10-15",
                person_table.c.id > 1
            )
        )
    )
    result_set = conn.execute(query_and).fetchall()
    print(result_set)
    conn.close()
