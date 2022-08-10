from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jbabajohn:jbabaPassword@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    
    
    def __repr__(self):
        return f'<Todo Id: {self.id}  Todo description: {self.description}>'



@app.route('/')
def index():
    todo = Todo.query.first()
    print("todo", todo)
    return f'Hello {todo.description}'

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')