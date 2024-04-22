from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#Создание таблиц Users и Dishes

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(VARCHAR(50), nullable=True)
    password = Column(VARCHAR(300), nullable=False)
    email = Column(VARCHAR(40))

    UniqueConstraint(username, name='username')
    UniqueConstraint(email, name='email')


class Dishes(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey(f'{User.__tablename__}.{User.id.name}'), nullable=False)
    dish = Column(VARCHAR(100), nullable=True)
    user = relationship('User', backref='dishes')
'''
class Recipes(Base):
    __tablename__ = 'recipes'
    id_recipe = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id_dish = Column()'''