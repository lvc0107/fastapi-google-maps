from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from app.settings import settings

Base = declarative_base()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


# --- User Table ---
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)  # Unsplash user id
    username = Column(String, nullable=False)
    name = Column(String)
    portfolio_url = Column(String)

    photos = relationship("Photo", back_populates="user")


# --- Photo Table ---
class Photo(Base):
    __tablename__ = "photos"

    id = Column(String, primary_key=True)  # Unsplash photo id
    created_at = Column(DateTime, default=datetime.utcnow)
    description = Column(Text)
    alt_description = Column(Text)
    url_full = Column(String)
    url_thumb = Column(String)

    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="photos")

    tags = relationship("Tag", back_populates="photo", cascade="all, delete-orphan")


# --- Tag Table ---
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    photo_id = Column(String, ForeignKey("photos.id"))
    photo = relationship("Photo", back_populates="tags")
