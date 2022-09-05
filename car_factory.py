from datetime import date
from typing import List

from car import Car

from batteries.spindler_battery import SpindlerBattery
from batteries.nubbin_battery import NubbinBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tires.carrigan_tires import CarriganTires
from  tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        battery = SpindlerBattery(last_service_date=last_service_date, current_service_date=current_date)
        engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine=engine, battery=battery, tires=tires)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        battery = SpindlerBattery(last_service_date=last_service_date, current_service_date=current_date)
        engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        tires = OctoprimeTires(tire_wear=tire_wear)
        return Car(engine=engine, battery=battery, tires=tires)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: List[float]) -> Car:
        battery = NubbinBattery(last_service_date=last_service_date, current_service_date=current_date)
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine=engine, battery=battery, tires=tires)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        battery = NubbinBattery(last_service_date=last_service_date, current_service_date=current_date)
        engine = WilloughbyEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        tires = OctoprimeTires(tire_wear=tire_wear)
        return Car(engine=engine, battery=battery, tires=tires)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        battery = NubbinBattery(last_service_date=last_service_date, current_service_date=current_date)
        engine = CapuletEngine(last_service_mileage=last_service_mileage, current_mileage=current_mileage)
        tires = CarriganTires(tire_wear=tire_wear)
        return Car(engine=engine, battery=battery, tires=tires)