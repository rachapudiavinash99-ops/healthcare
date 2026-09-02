from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(String)
