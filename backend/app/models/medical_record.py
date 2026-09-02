from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.core.database import Base

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    diagnosis = Column(Text)
    notes = Column(Text)
