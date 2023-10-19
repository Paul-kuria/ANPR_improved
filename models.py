from sqlalchemy import create_engine, Column, Integer, String, ForeignKey , VARCHAR
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base 

from database import Base 

class House(Base):
    __tablename__ = "houses"

    house_number = Column(Integer, primary_key=True)
    address = Column(String)
    tenants = relationship("Tenant", back_populates="house")

class Tenant(Base):
    __tablename__ = "tenants"
    tenant_id = Column(Integer, primary_key=True)
    name = Column(String)
    house_number = Column(Integer, ForeignKey("houses.house_number"))
    family_members = Column(String) # JSON or JSONB
    house = relationship("House", back_populates="tenant")

class Vehicle(Base):
    __tablename__ = "vehicles"
    car_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey("tenants.tenant_id"))
    plate_number = Column(VARCHAR(15), unique=True)
    vehicle_type = Column(String)
    tenant = relationship("Tenant", back_populates="vehicles")

class Guest(Base):
    __tablename__ = "guests"
    guest_id = Column(Integer, primary_key=True)
    name = Column(String)
    house_number = relationship("Guest", back_populates="house")
    plate_number = Column(VARCHAR(15), unique=True)
    vehicle_type = Column(String)

class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column(Integer, primary_key=True)
    name = Column(String)
    occupation = Column(String)
    building = Column(Integer, ForeignKey("buildings.building_id"))
    plate_number = Column(VARCHAR(15), unique=True)
    vehicle_type = Column(String)


class Building(Base):
    __tablename__ = "buildings"
    building_id = Column(Integer, primary_key=True)
    name = Column(String)
    staff = relationship("Staff", back_populates="buildings")