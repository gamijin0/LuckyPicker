from  application import db


class Bot(db.Model):
    __tablename__="Bots"
    #账号
    username = db.Column(db.String,primary_key=True)

    #cookies
    cookies = db.Column(db.String)

