from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        pass