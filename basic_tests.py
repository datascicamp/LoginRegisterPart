from app import db
from app.models import Account

if __name__ == '__main__':

    a = Account(
        account_email='Mike@example.com'
    )

    a.set_password('123456')

    print(a.check_password('123456'))
    db.session.add(a)
    db.session.commit()

    accounts = Account.query.all()
    print(accounts)
    # username = "Mike"
    # users = User.query.filter(User.username == username).all()
    # print(users)
    pass
