#!/usr/bin/python3
""" Doing database things """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():
    """ DB Storage serialization, dezerilaization """

    __engine = None
    __session = None

    bnb_classes = {
                'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
              }

    def __init__(self):
        #do we want to maniuplate the instance version of the attribute
        #or the class version, for both of these (self, or db)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            #if in the test directory, clear existing tables(for this session)
           Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        instance_dict = {}
        #If there is no class we go through the classes in the classes in filestorage
        #After we find the class we append it to the isstance.id and add it to the new dict
        if cls is None:
            for class_str, class_actual in DBStorage.bnb_classes.items():
                data = self.__session.query(class_actual)
                for instance in data:
                    instance_dict[class_str + '.' + instance.id] = class_actual.to_dict(instance)
            return instance_dict
        else:
                data = self.__session.query(cls.__tablename__)
                for instance in data:
                    instance_dict[cls.__name__ + '.' + instance.id] = cls.to_dict(instance)
                return instance_dict

    def new(self, obj):
        #add the object to the current db session
        self.__session.add(obj)

    def save(self):
        #save the object to the current db session
        self.__session.commit()

    def delete(self, obj=None):
        #delete the object to the current db session if object is present
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        #creating all tables in the database
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        #ending the session in mySQL
        self.session.close()
