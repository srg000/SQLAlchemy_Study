from init_db import sessionLocal, Person

with sessionLocal() as db:
    # add one record
    # person = Person(name='srg', address="unknown")
    # db.add(person)
    # db.commit()
    # db.refresh(person)
    # print(person)

    # add multyple record
    person_list = [
        Person(name='asdf', address="unknown"),
        Person(name='tom', address="unknown")
    ]
    db.add_all(person_list)
    db.commit()
