from serviceable import Serviceable 

class Car(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = None
        self.battery = None

    def needs_service(self):
        pass
