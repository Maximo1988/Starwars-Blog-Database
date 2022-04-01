import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50)) 
    mass = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    homeworld = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    favorite = relationship(FavsCharacters)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    favorite = relationship(FavsPlanets)
    characters_id = Column(Integer, ForeignKey('Characters.id'))
    characters = relationship(Characters)
    pilots_id = Column(Integer, ForeignKey('Pilots.id'))
    pilots = relationship(Pilots)

class Starships(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    name = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    favorite = relationship(FavsStarships)
    pilots_id = Column(Integer, ForeignKey('Pilots.id'))
    pilots = relationship(Pilots)

class FavsCharacters(Base):
    __tablename__ = 'FavsCharacters'
    id = Column(Integer, primary_key=True)
    Characters_Name = Column(String(50), ForeignKey('Characters.name'))
    Characters = relationship(Characters)
    User = relationship(User)

class FavsPlanets(Base):
    __tablename__ = 'FavsPlanets'
    id = Column(Integer, primary_key=True)
    Planets_Name = Column(String(50), ForeignKey('Planets.name'))
    Planets = relationship(Planets)
    User = relationship(User)

class FavsStarships(Base):
    __tablename__ = 'FavsStarships'
    id = Column(Integer, primary_key=True)
    Starships_Name = Column(String(50), ForeignKey('Starships.name'))
    Starships = relationship(Starships)
    User = relationship(User)

class Pilots(Base):
    __tablename__ = 'Pilots'
    id = Column(Integer, primary_key=True)
    Characters_Name = Column(String(50), ForeignKey('Characters.id'))
    Characters = relationship(Characters)
    Starship_Name = Column(String(50), ForeignKey('Starships.id'))
    Starships = relationship(Starships)
    Planets_Name = Column(String(50), ForeignKey('Planets.id'))
    Planets = relationship(Planets)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')