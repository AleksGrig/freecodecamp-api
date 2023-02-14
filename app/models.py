from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import true
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String(30), nullable=False)
  content = Column(String(150), nullable=False)
  published = Column(Boolean, server_default=true(), nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
  owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  owner = relationship("User")

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, nullable=False)
  email = Column(String(30), nullable=False, unique=True)
  password = Column(String(150), nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Vote(Base):
  __tablename__ = 'votes'

  user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
  post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)