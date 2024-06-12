from init_db import sessionLocal, User, Role


def create_record():
    with sessionLocal() as db:
        r1 = Role(name="add")
        r2 = Role(name="delete")

        u1 = User(name="doinb", password="111")
        u2 = User(name="lwx", password="222")
        u3 = User(name="crisp", password="333")

        u1.roles.append(r1)
        u1.roles.append(r2)
        u2.roles.append(r1)
        u3.roles.append(r2)
        db.add_all([u1, u2, u3])
        db.commit()


def search_user():
    with sessionLocal() as db:
        user = db.query(User).filter(User.id == 1).one()
        print(user)
        print(user.roles)


# create_record()
search_user()