from . import db
from faker import Faker
from flask_login import UserMixin, AnonymousUserMixin

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)

    def fake_data(self,cnt=100):
        fake = Faker()
        for i in range(cnt):
            u = User(name=fake.user_name())
            db.session.add(u)
            try:
                db.session.commit()
            except  :
                db.session.rollback()

from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))