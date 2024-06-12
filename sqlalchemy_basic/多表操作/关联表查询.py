from sqlalchemy import select

from init_db import engine, employee_table, department_table

with engine.connect() as conn:
    '''
    新增关联表信息
    '''
    # conn.execute(
    #     department_table.insert(), [
    #         {"name": "hr"}, {"name": "it"}
    #     ]
    # )
    #
    # conn.execute(
    #     employee_table.insert(), [
    #         {"department_id": 1, "name": "Jack"},
    #         {"department_id": 1, "name": "Tom"},
    #         {"department_id": 1, "name": "Mary"},
    #         {"department_id": 2, "name": "Smith"},
    #         {"department_id": 2, "name": "Rose"},
    #         {"department_id": 2, "name": "Leon"},
    #     ]
    # )
    # conn.commit()

    '''
    关联表查询
    '''
    join_part = employee_table.join(department_table, employee_table.c.department_id == department_table.c.id)
    # 查询两个关联表的全部字段
    join_sql_all_column = select(join_part).where(department_table.c.name == 'hr')
    # 查询单表的字段
    join_sql_one_table = select(employee_table).select_from(join_part).where(department_table.c.name == 'hr')
    result = conn.execute(join_sql_one_table).fetchall()
    print(result)