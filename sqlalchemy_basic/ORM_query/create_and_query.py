from sqlalchemy import select
from sqlalchemy.orm import aliased

from init_db import sessionLocal, Department, Employee


def create_record():
    with sessionLocal() as db:
        dep = Department(name="product")
        emp = Employee(department=dep, name='crisp')
        db.add(emp)
        db.commit()


# 查询单个类
def select_single_target():
    with sessionLocal() as db:
        # 可以先写sql，再执行
        query_sql = select(Department).order_by(Department.name)
        res = db.execute(query_sql)
        for item in res:
            print(item)


# 使用join函数联表查询（另一种方式是直接根据关联表内的属性来查）
def select_multiple():
    with sessionLocal() as db:
        # 可以先写sql，再执行
        # isouter=True表示开始外连接
        query_sql = select(Department, Employee).join(Employee.department, isouter=True)
        res = db.execute(query_sql)
        for item in res:
            print(item)


# 使用别名查询
def select_with_alias():
    with sessionLocal() as db:
        emp_cls = aliased(Employee, name="emp")
        dep_cls = aliased(Department, name="dep")
        # 可以先写sql，再执行
        query_sql = select(dep_cls, emp_cls).join(emp_cls.department.of_type(dep_cls))
        res = db.execute(query_sql)
        for item in res:
            print(item)


# 查询多个类中的个别字段
def select_fields():
    with sessionLocal() as db:
        # 可以先写sql，再执行
        query_sql = select(Department.name.label("dep_name"), Employee.name.label("emp_name")).join_from(
            Employee, Department
        )
        res = db.execute(query_sql)
        for item in res:
            print(item)


def where_obj():
    with sessionLocal() as db:
        dep = db.get(Department, 1)
        query_sql = select(Employee).where(Employee.department == dep)
        res = db.execute(query_sql)
        for item in res:
            print(item)


def select_contains():
    with sessionLocal() as db:
        emp = db.get(Employee,1)
        query_sql = select(Department).where(Department.employees.contains(emp))
        res = db.execute(query_sql)
        for item in res:
            print(item)


# create_record()
# select_single_target()
# select_multiple()
# select_with_alias()
select_fields()
