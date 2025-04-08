from app import db, app
from app.models import User, Post


app_context = app.app_context()
app_context.push()
u1 = User(username='cyrus', email='cyrus@example.com')
u1.set_password("cyrus")
db.session.add(u1)
p1 = Post(body='m', author=u1)
db.session.add(p1)

db.session.commit()
