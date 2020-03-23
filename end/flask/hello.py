from flask import Flask
# from SQLALchemy
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_ECHO'] = True

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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


def query():
    cs = Category.query.all()
    car = Category.query.filter_by(name='汽车').first()
    print(cs)
    print(car)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    # 操作数据库不需要运行项目
    app.run()
    # 生成数据库表 初始化 第一次运行
    # create_table()
    # 增加数据
    # add_user()
    # 查询数据
    # query()
    # 修改数据
    # update()
    # 删除数据
    # delete()
