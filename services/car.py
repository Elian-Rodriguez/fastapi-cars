from sqlalchemy.orm import Session
from models.car import SportsCar as SportsCarModel
from schemas.car import SportsCar


class SportsCarService():
    
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_cars(self):
        result = self.db.query(SportsCarModel).all()
        return result

    def get_car(self, id: int):
        result = self.db.query(SportsCarModel).filter(SportsCarModel.id == id).first()
        return result

    def get_cars_by_make(self, make: str):
        result = self.db.query(SportsCarModel).filter(SportsCarModel.make == make).all()
        return result

    def get_cars_by_year(self, year: int):
        result = self.db.query(SportsCarModel).filter(SportsCarModel.year == year).all()
        return result

    def create_car(self, car: SportsCar):
        if car.id is None:
            car_dict = car.dict()
            car_dict.pop('id')
            new_car = SportsCarModel(**car_dict)
        else:
            new_car = SportsCarModel(**car.dict())
        self.db.add(new_car)
        self.db.commit()
        return

    def update_car(self, id: int, data: SportsCar):
        car = self.db.query(SportsCarModel).filter(SportsCarModel.id == id).first()
        car.make = data.make
        car.model = data.model
        car.year = data.year
        car.horsepower = data.horsepower
        car.top_speed = data.top_speed
        self.db.commit()
        return

    def delete_car(self, id: int):
        self.db.query(SportsCarModel).filter(SportsCarModel.id == id).delete()
        self.db.commit()
        return
