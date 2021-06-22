#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)    
    __tablename__ = 'states'
    cities = relationship('City', cascade='all, delete-orphan', backref='state')

    @property
    def cities(self):
        """ Returns list of city instances, connected to state id """
        if getenv('HBNB_TYPE_STORAGE') == 'db':
        #ORM code to retrieve from table
            list_of_cities = []
            for instance in storage.all(City).values():
                if instance.state_id == self.id:
                    list_of_cities.append(instance)
            return list_of_cities
	else:
            return storage.all(State)
