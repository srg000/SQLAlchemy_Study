from sqlalchemy.orm import Session

from init_db import sessionLocal, Department, Employee


def create_record():
    with sessionLocal() as db:
        dep = Department(name="it")
        emp = Employee(department=dep, name='lwx')
        db.add(emp)
        db.commit()


def query_emp():
    with sessionLocal() as db:
        emp = db.query(Employee).filter(Employee.id == 1).one()
        print(emp)
        print(emp.department)


def query_dep():
    with sessionLocal() as db:
        dep = db.query(Department).filter(Department.id == 1).one()
        print(dep)
        print(dep.employees)


def query_all():
    with sessionLocal() as db:
        emp = db.query(Employee).all()
        for item in emp:
            print(item)


def delete_emp():
    with sessionLocal() as db:
        db.query(Employee).filter(Employee.id == 2).delete()

# create_record()
# query_emp()
# query_all()
delete_emp()
