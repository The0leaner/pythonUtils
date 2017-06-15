# -*- coding: utf-8 -*-
'''
SQLAlchemy in four steps
1 Configuration
2 Class
3 Table
4 Mapper
connects the columns of our table to the class that represents
映射器
'''

'''
at beginning of file
import all modules needed
creates instance of declarative base

at the end of file
connect to configurate the database
'''

import sys

from sqlalchemy import  Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import  declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

#to let sqlalchemy know that we are special SQLAchemy
# classes that correspond to tables in our databases
Base = declarative_base()


'''
primary_key (true) indicates a value that 
we can use to uniquely identify each row of db table

foreign_key we can use to reference a row in 
a different table provided that a relation
exists between the two of them
'''
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer , primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):
    __talename__ = 'menu_item'


    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    desciption = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


###### insert at end of file######
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
'''
newEntry = ClassNmae(property = "", ...)
session.add(newEntry)
session.commmit()
'''

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commmit()
# for making sure it owrked
session.query(Restaurant).all()

#test
firstRestaurant = session.query(Restaurant).first()
firstRestaurant.name

