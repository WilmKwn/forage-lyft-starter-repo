from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, array):
        super().__init__(array)

    def needs_service(self):
        sum = 0
        for i in range(len(self.array)):
            sum += self.array[i]
        return sum >= 3