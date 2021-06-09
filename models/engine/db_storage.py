#!/usr/bin/python3
""" Doing database things """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from sqlalchemy import create_engine, session
from sqlalchemy import Column, Integer, String
import os 
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage(Base):
    """ DB Storage serialization, dezerilaization """

    __engine = None
    __session = None

    def __init__(self):
        #do we want to maniuplate the instance version of the attribute
        #or the class version, for both of these (self, or db)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB, pool_pre_ping=True)
        if os.environ['HBNB_ENV'] == 'test':
            #if in the test directory, clear existing tables(for this session)
            drop_all(self.__session)

    def all(self, cls=None):
        instance_dict = {}
        #If there is no class we go through the classes in the classes in filestorage
        #After we find the class we append it to the isstance.id and add it to the new dict
        if cls == None:
                for class_str, class_name in FileStorage.classes.items():
                    data = self.__session.query(class_name)
                    for instance in data:
                        instance_dict[class_str + '.' + instance.id] = class_name.to_dict(instance)
                return instance_dict
        else:
                data = self.__session.query(cls)
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

    def reload(self):
        #creating all tables in the database
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))


