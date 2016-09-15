from  application import db


class Bot(db.Model):
    __tablename__="Bots"
    #主键
    id = db.Column(db.String,primary_key=True)
    #姓名
    name = db.Column(db.String,nullable=False)