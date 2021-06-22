#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
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
        #ORM code to retrieve from table
        from models import storage
        list_of_cities = []
        for instance in storage.all(City).values():
            if instance.state_id == self.id:
                list_of_cities.append(instance)
        return list_of_cities
