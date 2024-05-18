#!/usr/bin/python3
"""
This module contains the engine class used to initiate transactions with
postgresql database
"""
from schema import Base
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy_utils import force_auto_coercion
from sqlalchemy.orm import Session

load_dotenv()

class Engine():
    """Engine class to interact with sql database"""
    __db_name = getenv("DB_NAME")
    __db_user = getenv("DB_USER")
    __db_port = getenv("DB_PORT")
    __db_hostname = getenv("DB_HOSTNAME")
    __db_password = getenv("DB_PASSWORD")

    print("DB_NAME:", getenv("DB_NAME"))
    print("DB_USER:", getenv("DB_USER"))
    print("DB_PORT:", getenv("DB_PORT"))
    print("DB_HOSTNAME:", getenv("DB_HOSTNAME"))
    print("DB_PASSWORD:", getenv("DB_PASSWORD"))

    def __init__(self):
        force_auto_coercion()
        default_db_port = "5432" # default port for postgresql
        self.__db_port = getenv("DB_PORT", default_db_port)
        self.db_url = (f"postgresql+psycopg2://{self.__db_user}:"
                       f"{self.__db_password}@{self.__db_hostname}:"
                       f"{self.__db_port}/{self.__db_name}")

        self.__engine = create_engine(self.db_url, echo=False)
        self.reload()

    def reload(self):
        """commit and establish connection with the database"""
        Base.metadata.create_all(bind=self.__engine)
        self.__session = Session(bind=self.__engine, expire_on_commit=False)

    def get(self, orm_class, uuid):
        """method to get a new ORM instance"""
        return self.__session.query(orm_class).first(id=uuid)

    def post(self, orm_class, *args, **kwargs):
        """method to create a new ORM instance"""
        obj = orm_class(**kwargs)
        self.__session.add(obj)
        return obj

    def save(self):
        """method to write changes to the database"""
        self.__session.commit()
        self.reload()

    def close(self):
        """method to close the connection to the database"""
        self.__session.close()

    def __call__(self):
        """method that allows the class be used like a function"""
        try:
            yield self
        finally:
            self.close()
