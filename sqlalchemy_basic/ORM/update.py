from init_db import sessionLocal, Person

with sessionLocal() as db:
    '''
    修改单条记录
    '''
    # 方法一
    person = db.query(Person).filter(Person.id == 1).one()
    person.address = 'update_address'
    db.commit()
    db.refresh(person)
    print(person.address)

    # 方法二
    db.query(Person).filter(Person.id == 2).update({Person.address: 'test_2'})
    db.commit()

    '''
    批量修改
    '''
    db.query(Person).filter(Person.id > 2).update({
        Person.address: "update_id>2"
    })
    db.commit()




