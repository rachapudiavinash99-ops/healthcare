from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.core.database import Base

class Prescription(Base):
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    medication = Column(String)
    dosage = Column(String)
