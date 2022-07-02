from .database import Base
from sqlalchemy import Column, Integer,String, Float, Boolean, Table
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.types import Date,ARRAY
from sqlalchemy.orm import relationship

#models
class User(Base):
    __tablename__ ='user'
    user_id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String, nullable=False)
    password = Column(String, nullable=False)
    name= Column( String, nullable=False)
    dob=Column(Date)
    phone=Column(String, nullable=False)
    address=Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Category(Base):
    __tablename__='category'
    id= Column(Integer, primary_key=True, nullable=False)
    name =Column(String, nullable=False)
    desc = Column(String)

class Review(Base):
    __tablename__='review'
    id= Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False) #TODO make it a FK
    date = Column(Date, nullable=False)
    review =Column(String, nullable=False) 
    product_id = Column(Integer, nullable=False) #TODO make it a FK
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Saved(Base):
    __tablename__='saved'
    id= Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False) #TODO make it a FK
    product_id = Column(Integer, nullable=False) #TODO make it a FK


class Product(Base):
    __tablename__='product'
    product_id= Column(Integer, primary_key=True, nullable=False)
    name= Column(String, nullable=False)
    price =Column(Float, nullable=False)
    quantity = Column( String)
    category_id = Column(Integer,  nullable=False) #TODO make it a FK
    image_url = Column(String, nullable=False)
    image_banner = Column(String, nullable=False)

class Order(Base):
    __tablename__='order'
    order_id= Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False) #TODO make it a FK
    items =Column(ARRAY(Integer), nullable=False)
    payment_made=Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )

class Payment(Base):
    __tablename__='payment'
    id= Column(Integer, primary_key=True, nullable=False)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, nullable=False) #TODO make it a FK
    order_id= Column(Integer,  nullable=False) #TODO make it a FK
    method =Column( String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text( 'NOW()') )



