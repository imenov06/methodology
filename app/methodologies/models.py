from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from app.database.db_connect import Base


class Methodologies(Base):
    __tablename__ = "methodologies"

    id = Column(Integer, primary_key=True)

    title = Column(String(256), nullable=False)
    description = Column(String(4096), nullable=True)
    avatar_url = Column(String(1024), nullable=True)
    is_published = Column(Boolean, default=True, nullable=False)



class ImagesInMethodologies(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)

    url = Column(String(1024), nullable=False)
    method_id = Column(Integer, ForeignKey("methodologies.id", ondelete="CASCADE"))

