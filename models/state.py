#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import city
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)    
    __tablename__ = "states"
    __cities__ = relationship("City", cascade="all, delete-orphan")

    @property
    def cities(self):
        """ Returns list of city instances, connected to state id """
        #ORM code to retrieve from table
        return self.__cities__
