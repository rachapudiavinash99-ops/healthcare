from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.core.database import Base

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    total_amount = Column(Float)
    status = Column(String)
