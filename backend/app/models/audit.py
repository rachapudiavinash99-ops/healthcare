from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.core.database import Base
from datetime import datetime

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
