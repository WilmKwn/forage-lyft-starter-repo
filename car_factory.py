from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

from car import Car

class CarFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array)
        return Car(last_service_date, engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array)
        return Car(last_service_date, engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tires_array):
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_array)
        return Car(last_service_date, engine, battery, tires)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_array)
        return Car(last_service_date, engine, battery, tires)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_array)
        return Car(last_service_date, engine, battery, tires)
    