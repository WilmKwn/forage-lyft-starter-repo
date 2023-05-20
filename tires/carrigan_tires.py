from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, array):
        super().__init__(array)

    def needs_service(self):
        for i in range(len(self.array)):
            if self.array[i] >= 0.9:
                return True
        return False