from init_db import engine, person as person_table

with engine.connect() as conn:
    # 修改
    update_sql = person_table.update().values(address="test"). \
        where(person_table.c.id == 1)
    conn.execute(update_sql)
    conn.commit()

    # 删除
    delete_sql = person_table.delete().where(person_table.c.id == 4)
    conn.execute(delete_sql)
    conn.commit()
