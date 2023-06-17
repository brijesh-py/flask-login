from app import db, UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    def __init__(self, username, email, password, created_at):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)

    def check_password(self, password):
        return self.password == password

    def is_active(self):
        return True

    def is_authenticated(self):
        return True 
    
    def __str__(self):
        return f"<User {self.username}>"