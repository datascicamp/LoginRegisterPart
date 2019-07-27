from app import db
from app.models import User

if __name__ == '__main__':

    u = User(
        username='Mike',
        email='Mike@example.com',
        phone_number='11311311113',
    )

    u.set_password('123456')

    print(u.check_password('123456'))
    db.session.add(u)
    db.session.commit()

    users = User.query.all()
    print(users)
    # username = "Mike"
    # users = User.query.filter(User.username == username).all()
    # print(users)
    pass
