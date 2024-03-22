#!/usr/bin/python3
"""A database for Cities"""
from sqlalchemy import Integer, create_engine, Column, String, ForeignKey
from model_state import Base, State


class City(Base):
    """My City Table In DB"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
