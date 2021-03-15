import os
from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    ARRAY,
    TIMESTAMP,
    Table,
    MetaData,
    DateTime,
    ForeignKey,
    Float
)
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from pytz import timezone

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

metadata = MetaData()
Base = declarative_base(metadata=metadata)
fmt = "%Y-%m-%d %H:%M:%S %Z%z"

db_path = {
    'dialect':'postgresql',
    'username':'postgres',
    'password':'8949',
    'host':'localhost:5432',
    'database_name':'FUAPP'
}
database_path = f'{db_path["dialect"]}://{db_path["username"]}:{db_path["password"]}@{db_path["host"]}/{db_path["database_name"]}'
db = SQLAlchemy(metadata=metadata)

def setup_db(app, database_path=database_path):
    '''
    binds flask application and SQLAlchemy service
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

# topic_post_assiciation_table = Table() #Implemented when relationships have been set

class User(db.Model):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    fName = Column(String(150), nullable=False)
    lName = Column(String(150), nullable=False)
    uName = Column(String(150), nullable=False)
    dateCreated = Column(DateTime(), nullable=False)

    def __init__(self, fName, lName, uName):
        self.fName = fName
        self.lName = lName
        self.uName = uName
        self.dateCreated = datetime.now(timezone('UTC')).astimezone('US/Pacific')

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
    
    def update(self):
        try:
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
    
    def format(self):
        return{
            'id':self.id,
            'fName':self.fName,
            'lName':self.lName,
            'uName':self.uName,
            'dateCreated':self.dateCreated
        }

class KeyWord(db.Model):
    __tablename__ = 'KeyWord'

    id = Column(String, primary_key=True) #id counts as the title of the word as well as the primary key
    numFU = Column(Integer, nullable=False)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
        
    def update(self):
        try:
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as E:
            print(E)
            db.session.rollback()
    
    def format(self):
        return{
            'id':self.id,
            'numFU':self.numFU
        }