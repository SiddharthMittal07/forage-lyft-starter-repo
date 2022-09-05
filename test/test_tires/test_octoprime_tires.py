import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear =  [0.9, 0.5, 1.0, 0.8]
        tires = OctoprimeTires(tire_wear=tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.1, 0.5, 0.8, 0.4]
        tires =  OctoprimeTires(tire_wear=tire_wear)
        self.assertFalse(tires.needs_service())