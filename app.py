from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# подключаем SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# создаём таблицы (один раз)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("Window.html")

# обработчик регистрации
@app.route("/register", methods=["POST"])
def register():
    login = request.form["login"]
    email = request.form["email"]
    password = request.form["password"]

    # создаём нового пользователя
    new_user = User(login=login, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return f"Пользователь {login} успешно зарегистрирован!"

if __name__ == "__main__":
    app.run(debug=True)
