from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'have a nice day'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()