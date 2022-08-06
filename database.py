from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

SQL_USER = 'root'
SQL_PASS = ''
SQL_DB = 'laraibdb'
SQL_HOST = 'localhost'

app = Flask(__name__)
app.secret_key = "login key"

# database
db_url = 'mysql+pymysql://' + SQL_USER + '@' + SQL_HOST + '/' + SQL_DB
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize db
db = SQLAlchemy(app)

from web.user_api import *
from web.car_api import *

app.register_blueprint(user_blueprint)
app.register_blueprint(car_blueprint)

# db migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Run Server
if __name__ == '__main__':
    manager.run()
