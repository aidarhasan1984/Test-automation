import requests
import pytest
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    create_timestamp = Column(DateTime, default=datetime.now)
    change_timestamp = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    first_name = Column(String(20))
    last_name = Column(String(20))
    middle_name = Column(String(20))
    phone = Column(String(15))
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer)

url = "https://x-clients-be.onrender.com"

def test_get_employee():

    engine = create_engine('postgres://x_clients_user:[axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com]/x_clients')
    Session = sessionmaker(bind=engine)
    session = Session()
    employee = Employee(first_name="John", last_name="Doe", email="john.doe@example.com", company_id=1)
    session.add(employee)
    session.commit()
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url + "/employee", headers=headers)
    assert response.status_code == 200
    
    session.delete(employee)
    session.commit()
    