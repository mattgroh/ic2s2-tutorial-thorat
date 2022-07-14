from webapp import db, app
db.create_all(app=app) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
