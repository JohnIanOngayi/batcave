#!/usr/bin/python3
from enum import unique
from sqlalchemy import Column, ForeignKey, Nullable, String, DateTime, Table, create_engine
from sqlalchemy.orm import backref, declarative_base, relationship, sessionmaker
from datetime import datetime
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    id = Column(String(length=60), primary_key=True, default=lambda: str(uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.now())


class User(BaseModel, Base):
    __tablename__ = "users"
    first_name = Column(String(length=60), nullable=True)
    last_name = Column(String(length=60), nullable=True)
    email = Column(String(length=80), nullable=False, unique=True)
    places = relationship('Place', backref=backref('user'), cascade='all, delete')
    reviews = relationship('Review', backref=backref('user'), cascade='all, delete')


class Place(BaseModel, Base):
    __tablename__ = "places"
    user_id = Column(String(length=60), ForeignKey("users.id"), nullable=False)
    city_id = Column(String(length=60), ForeignKey("cities.id"), nullable=False)
    name = Column(String(length=80), nullable=False)
    description = Column(String(length=10240), nullable=True)
    reviews = relationship('Review', backref=backref('place'), cascade='all, delete')


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(length=1024), nullable=False)


class PlaceAmenity():
    __tablename__ = "place_amenities"
    amenity_id = Column(ForeignKey('amenities.id'))
    place_id = Column(ForeignKey('places.id'))
    amenities = relationship('Amenity', back_populates='places')
    places = relationship('Place', back_populates='amenities')


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(length=60), nullable=False)
    cities = relationship('City', backref=backref('state'), cascade='all, delete')


class City(BaseModel, Base):
    __tablename__ = "cities"
    name = Column(String(length=60), nullable=False)
    state_id = Column(String(length=60), ForeignKey("states.id"), nullable=False)
    places = relationship('Place', backref=backref('city'), cascade='all, delete')


class Review(BaseModel, Base):
    __tablename__ = "reviews"
    text = Column(String(length=10240), nullable=False)
    user_id = Column(String(length=60), ForeignKey("users.id"), nullable=False)
    place_id = Column(String(length=60), ForeignKey("places.id"), nullable=False)


db = f"sqlite:////home/johnian/batcave/mypysql/socialDB.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

johnian = User(email='johnie@richierichrich')
ongayi = User(email='ongayi@richierichrich')
texas = State(name='Texas')
california = State(name='California')
new_jersey = City(name='New Jersey', state=california)
ohio = City(name='Ohio', state=texas)
wifi = Amenity(name='WiFi')
balcony = Amenity(name='Balcony')
my_home = Place(name='MyHome', user=johnian, city=ohio)
your_home = Place(name='YourHome', user=johnian, city=new_jersey)
review_1 = Review(text='Mui phenomeno', user=ongayi, place=your_home)
session.add_all([johnian, ongayi, review_1, texas, california, new_jersey, ohio, wifi, balcony, my_home, your_home])
session.commit()
session.close()
