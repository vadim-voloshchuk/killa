from __main__ import db

class Files(db.Model):
    file_id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.dialects.mysql.MEDIUMBLOB, nullable=False)
    