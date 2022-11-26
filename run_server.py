import bottle
from bottle import run, template, redirect, static_file, request

from config import config
from models import Base, Sentence, User

from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from bottle_login import LoginPlugin

engine = create_engine(f"sqlite:///{config['dbfile']}")

app = bottle.Bottle()
dbplugin = sqlalchemy.Plugin(engine, Base.metadata, keyword="db", create=True, commit=True)
app.install(dbplugin)

app.config['SECRET_KEY'] = 'secret'
login = app.install(LoginPlugin())

@login.load_user
def load_user_by_id(id, db):
    user = db.query(User).get(id)
    return user

@app.route('/')
def index():
    current_user = login.get_user()
    return current_user.name

@app.route('/signout')
def signout():
    # Implement logout
    login.logout_user()
    return redirect('/')

@app.route('/signin')
def signin():
    # Implement login (you can check passwords here or etc)
    user_id = int(request.GET.get('user_id'))
    login.login_user(user_id)
    return redirect('/')


@app.get("/")
def index(db):
    sentences = db.query(Sentence).all()
    return template("index", sentences=sentences)


@app.get("/sentences/:id")
def get_sentence(id, db):
    sentence = db.query(Sentence).get(id)
    return template("sentence",  sentence=sentence)



@app.get("/flush")
def flush(db):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Populate corpus
    with open("./data/corpus-min.txt") as f:
        lines = f.readlines()
        for line in lines:
            snt = Sentence()
            snt.text = line
            db.add(snt)
    db.commit()

    redirect("/")

@app.route('/<filename:path>')
def serve_static(filename, path="False"):
    return static_file(filename, root='public/')





if __name__ == '__main__':
    run(host=config["host"], port=config["port"], app=app, debug=config["debug"], reloader=config["reloader"])