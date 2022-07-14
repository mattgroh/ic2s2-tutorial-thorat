from datetime import datetime
# from . import db
# from sqlalchemy.sql import func

# class Survey(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     referral_source = db.Column(db.String(150))
#     study_id = db.Column(db.String(150))
#     a0 = db.Column(db.String(150))
#     a1 = db.Column(db.String(150))
#     a2 = db.Column(db.String(150))
#     a3 = db.Column(db.String(150))
#     a4 = db.Column(db.String(150))
#     a5 = db.Column(db.String(150))
#     a6 = db.Column(db.String(150))
#     a7 = db.Column(db.String(150))
#     faithful = db.Column(db.String(150))
#     time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

# class Guess(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
#     assignment = db.Column(db.String(150))
#     user_id = db.Column(db.Integer)
#     image_id = db.Column(db.String(150))
#     correct_guess = db.Column(db.Integer)
#     guess = db.Column(db.String(150))
#     differential_two = db.Column(db.String(150))
#     differential_three = db.Column(db.String(150))
#     guess_int = db.Column(db.Integer)
#     guess_round = db.Column(db.Integer)
#     seen = db.Column(db.Integer)
#     ip = db.Column(db.String(150))
#     user_platform = db.Column(db.String(150))
#     user_browser = db.Column(db.String(150))
#     biopsy = db.Column(db.Integer)
#     dermatologist = db.Column(db.Integer)
#     model_selection = db.Column(db.Integer)
#     changer = db.Column(db.String(150))

#     