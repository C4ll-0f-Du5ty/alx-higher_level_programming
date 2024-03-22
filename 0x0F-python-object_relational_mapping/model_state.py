#!/usr/bin/python3
"""To Make a State Table in my database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """My State Table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
