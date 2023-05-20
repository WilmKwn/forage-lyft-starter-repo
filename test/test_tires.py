import unittest
from datetime import datetime

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarrigan(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        tires = CarriganTires([0.8, 0.8, 0.8, 0.9])
        self.assertTrue(tires.needs_service())

    def test_battery_should_not_be_serviced(self):
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        self.assertfalse(tires.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        tires = OctoprimeTires([0.7, 0.7, 0.7, 0.9])
        self.assertTrue(tires.needs_service())

    def test_battery_should_not_be_serviced(self):
        tires = OctoprimeTires([0.7, 0.7, 0.7, 0.8])
        self.assertFalse(tires.needs_service())