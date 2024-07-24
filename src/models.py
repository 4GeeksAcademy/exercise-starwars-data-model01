import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password  = Column(String(30), nullable=False)
    date_of_suscription = Column(Date, nullable=False)
    favorites = relationship('Favorites', backref='favorites', lazy=True)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    population = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    favorite = relationship('Favorites', backref='favorites', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    model = Column(String(50), nullable=False)
    size = Column(String(50), nullable=False)
    favorites = relationship('Favorites', backref='favorites', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    gender = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    favorites = relationship('Favorites', backref='favorites', lazy=True)

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
