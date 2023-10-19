from pydantic import BaseModel 
from typing import List 
import uuid 

# Schemas for the tenant model
class TenantBase(BaseModel):
    name: str 
    house_number: int 
    num_cars: int 

class TenantCreate(TenantBase):
    pass 

class Tenant(TenantBase):
    id: int 


# Schemas for the car model
class CarBase(BaseModel):
    plate_number: str 
    type: str 

class CarCreate(CarBase):
    pass 

class Car(CarBase):
    pass 


# Schemas for the house model 
class HouseBase(BaseModel):
    house_number: int 

class HouseCreate(HouseBase):
    pass 

class House(HouseBase):
    id: int 
    tenants: List[Tenant] = [] 


# Schema for the guest model
class GuestBase(BaseModel):
    name: str 
    house_number: int 
    car_plate_number: str 
    car_type: str 

class GuestCreate(GuestBase):
    pass 

class Guest(GuestBase):
    id: int 


# Schema for the staff model 
class StaffBase(BaseModel):
    name: str 
    occupation: str 
    building: str 
    car_plate_name: str 
    car_type: str 

class StaffCreate(StaffBase):
    pass 

class Staff(StaffBase):
    id: int 
    
