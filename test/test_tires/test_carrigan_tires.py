import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear =  [0.5, 0.3, 1.0, 0.8]
        tires = CarriganTires(tire_wear=tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.1, 0.5, 0.8, 0.4]
        tires =  CarriganTires(tire_wear=tire_wear)
        self.assertFalse(tires.needs_service())