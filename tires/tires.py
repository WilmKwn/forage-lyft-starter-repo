from abc import ABC, abstractmethod

class Tires:
    def __init__(self, array):
        self.array = array
        pass
    
    @abstractmethod
    def needs_service(self):
        pass