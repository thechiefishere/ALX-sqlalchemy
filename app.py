from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jbabajohn:jbabaPassword@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app);

class Street(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f'<Street Id: {self.id}  Street name: {self.name}>'
    
db.create_all()


@app.route('/')
def index():
    street = Street.query.first()
    print("street", street)
    return f'Hello {street.name}'

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')