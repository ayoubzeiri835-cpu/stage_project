from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    timezone = Column(String, default="UTC")
    working_hours = Column(String)  # E.g., "09:00-17:00"

    tasks = relationship("Task", back_populates="user")
    memories = relationship("Memory", back_populates="user")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    priority = Column(String)  # E.g., "High", "Medium", "Low"
    deadline = Column(DateTime)
    duration = Column(Integer)  # Duration in minutes
    status = Column(String, default="Pending") # E.g., "Pending", "In Progress", "Completed"
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="tasks")


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    # Could also link to User if needed, though not explicitly in MD


class Memory(Base):
    __tablename__ = 'memories'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    embedding = Column(String)  # Typically stored as an array of floats, string placeholder or Vector type if pgvector used

    user = relationship("User", back_populates="memories")
