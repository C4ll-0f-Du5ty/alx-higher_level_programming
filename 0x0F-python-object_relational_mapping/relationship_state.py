#!/usr/bin/python3
"""To Make a State Table in my database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(MetaData=mymetadata)


class State(Base):
    """My State Table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
    # Relationship with City
