
from config.database import Session
from services.car import SportsCarService
from schemas.car import SportsCar
from models.car import SportsCar  as ModelSportsCar

cars = [

    {
        "id": 1,
        "make": "Ferrari",
        "model": "458 Italia",
        "year": 2015,
        "horsepower": 570,
        "top_speed": 202
    },
    {
        "id": 2,
        "make": "Lamborghini",
        "model": "Aventador",
        "year": 2018,
        "horsepower": 740,
        "top_speed": 217
    },
    {
        "id": 3,
        "make": "Porsche",
        "model": "911 Turbo S",
        "year": 2021,
        "horsepower": 640,
        "top_speed": 205
    },
    {
        "id": 4,
        "make": "McLaren",
        "model": "720S",
        "year": 2020,
        "horsepower": 710,
        "top_speed": 212
    },
    {
        "id": 5,
        "make": "Bugatti",
        "model": "Chiron",
        "year": 2022,
        "horsepower": 1500,
        "top_speed": 304
    },
    {
        "id": 6,
        "make": "Koenigsegg",
        "model": "Agera RS",
        "year": 2018,
        "horsepower": 1160,
        "top_speed": 278
    },
    {
        "id": 7,
        "make": "Ford",
        "model": "Mustang Shelby GT500",
        "year": 2022,
        "horsepower": 760,
        "top_speed": 180
    },
    {
        "id": 8,
        "make": "Chevrolet",
        "model": "Corvette Stingray",
        "year": 2022,
        "horsepower": 490,
        "top_speed": 184
    },
    {
        "id": 9,
        "make": "Dodge",
        "model": "Challenger Hellcat Redeye",
        "year": 2021,
        "horsepower": 797,
        "top_speed": 203
    },
    {
        "id": 10,
        "make": "Aston Martin",
        "model": "DBS Superleggera",
        "year": 2022,
        "horsepower": 715,
        "top_speed": 211
    },
    {
        "id": 11,
        "make": "BMW",
        "model": "M5 Competition",
        "year": 2022,
        "horsepower": 617,
        "top_speed": 180
    },
    {
        "id": 12,
        "make": "Mercedes-Benz",
        "model": "AMG GT R Pro",
        "year": 2022,
        "horsepower": 577,
        "top_speed": 198
    },
    {
        "id": 13,
        "make": "Nissan",
        "model": "GT-R Nismo",
        "year": 2022,
        "horsepower": 600,
        "top_speed": 205
    }
]


def load_data_cars(): 
    for car in cars:
        c = SportsCar(id=car['id'], make=car['make'], model=car['model'], year=car['year'], horsepower=car['horsepower'], top_speed=car['top_speed'])
        db = Session()
        SportsCarService(db).create_car(c)


