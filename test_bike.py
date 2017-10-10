import unittest
from bike import Bike

class BikeTestCase(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_default_bike_broken_state(self):
        self.assertEqual(self.bike.is_damaged, False)

    def test_can_be_damaged(self):
        self.bike.damage()
        self.assertEqual(self.bike.is_damaged, True)

    def test_can_be_fixed(self):
        self.bike.damage()
        self.bike.fix()
        self.assertEqual(self.bike.is_damaged, False)

unittest.main()