from .utils import *
from sqlalchemy.orm import relationship, backref


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    c_id = db.Column("cid", db.ForeignKey("category.id", ondelete='CASCADE'), nullable=False)
    category = db.relationship("Category", backref="books")

    def __repr__(self):
        return self.name


class Category(db.Model):
    # id = db.Colum(name="id", type=db.Integer(), primary_key=True, autoincrement=True)
    # name = db.Colum(name="id", type=db.String(50), nullable=False, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return self.name


def create_table():
    db.create_all()


# 增删改查
def add_user():
    car = Category(name='汽车')
    house = Category(name='房产')
    # 增加数据
    db.session.add(car)
    db.session.add(house)
    # 提交
    db.session.commit()


def delete():
    c = Category.query.get(1)
    db.session.delete(c)
    db.session.commit()


def update():
    c = Category.query.get(2)
    c.name = "旅游"
    db.session.commit()
