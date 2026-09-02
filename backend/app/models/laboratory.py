from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class LabTest(Base):
    __tablename__ = 'lab_tests'
    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    result = Column(String)
