from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

main_app = Flask(__name__)

main_app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
main_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql:3306@localhost/api'
main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = false

db = SQLAlchemy(main_app)


from web.cars import cars_blueprint
from web.users import users_blueprint

main_app.register_blueprint(cars_blueprint)
main_app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    # create new tables in database
    db.create_all()
    main_app.run()
