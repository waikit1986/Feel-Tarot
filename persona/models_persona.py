from db.database import Base
from sqlalchemy import UUID, Column, DateTime, String, INT, ForeignKey, func
import uuid


class Persona(Base):
    __tablename__ = "personas"
    
    id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, ForeignKey("users.username", ondelete="CASCADE", onupdate="CASCADE"), unique=True, index=True, nullable=False)
    age = Column(INT, nullable=False)
    bio = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

