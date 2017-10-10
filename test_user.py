import unittest
from user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        bike = Bike()
        bike = unittest.mock
        self.user = User(bike)

    def test_default_does_not_have_bike(self):
        user = User()
        self.assertEqual(user.bike, None)

    def test_can_have_bike(self):
        self.assertEqual(isinstance(self.user.bike, Bike), True)

    def test_can_damage_bike(self):
        self.user.damage_bike()
        self.assertEqual(self.user.bike.is_damaged, True)

    def test_can_lose_bike(self):
        self.user.lose_bike()
        self.assertEqual(self.user.bike, None)

unittest.main()