from init_db import sessionLocal, Person

with sessionLocal() as db:
    person = Person(name="test")
    db.add(person)
    db.commit()