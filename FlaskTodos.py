from flask import Flask, render_template, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.debug = True
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=False)
    is_done = db.Column(db.Boolean)

    def __init__(self, text, is_done=False):
        self.text = text
        self.is_done = is_done

    def __repr__(self):
        return '<Todo {}, completed {}>'.format(self.text, self.is_done)


@app.route('/')
@app.route('/index')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def addtodo():
    text = request.form['text']
    db.session.add(Todo(text=text))
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
