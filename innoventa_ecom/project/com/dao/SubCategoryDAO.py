# from django.db import models
from project.com.dao import con_db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = con_db()
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

class CategoryDAO(Base):
    __tablename__ = 'categorymaster'

    categoryId = Column(Integer, primary_key=True)
    categoryName = Column(String)

    def searchCategory(self):
        results = session.add(CategoryDAO('Jainish'))
        return results


