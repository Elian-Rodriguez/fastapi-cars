from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class SportsCar(Base):
    __tablename__ = "sports_cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    horsepower = Column(Integer)
    top_speed = Column(Float)
