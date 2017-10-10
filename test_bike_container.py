import unittest
from bike_container import BikeContainer
from bike import Bike

def add_bikes_to(holder, count, damaged_bikes = True):
    for num in range(0, count):
        bike = Bike()
        if damaged_bikes == False:
            bike.damage()
        holder.dock(bike)

class BikeTestCase(unittest.TestCase):
    def setUp(self):
        damaged_bike = Bike()
        damaged_bike.damage()
        self.bike_container = BikeContainer(20)
        self.other_container = BikeContainer(20)
        self.bike = Bike()
        self.damaged_bike = damaged_bike

    def test_default_capacity(self):
        bike_container = BikeContainer()
        self.assertEqual(bike_container.capacity, 10)

    def test_specifying_capacity(self):
        self.assertEqual(self.bike_container.capacity, 20)

    def test_should_dock_bike(self):
        self.bike_container.dock(self.bike)
        self.assertEqual(self.bike_container.total_count(), 1)

    def test_should_release_bike(self):
        self.bike_container.dock(self.bike)
        self.bike_container.release(self.bike)
        self.assertEqual(self.bike_container.is_empty(), True)

    def test_should_know_the_total_amount_of_bikes_it_holds(self):
        self.bike_container.dock(self.bike)
        self.bike_container.dock(self.damaged_bike)
        self.assertEqual(self.bike_container.total_count(), 2)

    def test_should_know_the_amount_of_fixed_bikes_it_holds(self):
        self.bike_container.dock(self.bike)
        self.bike_container.dock(self.damaged_bike)
        self.assertEqual(self.bike_container.fixed_count(), 1)        

    def test_should_know_the_amount_of_broken_bikes_it_holds(self):
        self.bike_container.dock(self.bike)
        self.bike_container.dock(self.damaged_bike)
        self.assertEqual(self.bike_container.damaged_count(), 1)        

    def test_should_know_when_full(self):
        add_bikes_to(self.bike_container, self.bike_container.capacity, False)
        self.assertEqual(self.bike_container.is_full(), True)

    def test_should_know_when_empty(self):
        self.assertEqual(self.bike_container.is_empty(), True)

    def test_should_give_fixed_bikes_to_another_container(self):
        add_bikes_to(self.bike_container, 10)
        add_bikes_to(self.bike_container, 10, False)
        self.bike_container.release_fixed_bikes_to(self.other_container)
        self.assertEqual(self.bike_container.total_count(), 10)
        self.assertEqual(self.bike_container.damaged_count(), 10)
        self.assertEqual(self.bike_container.fixed_count(), 0)
        self.assertEqual(self.other_container.fixed_count(), 10)

    def test_should_give_damaged_bikes_to_another_container(self):
        add_bikes_to(self.bike_container, 5)
        add_bikes_to(self.bike_container, 5, False)
        self.bike_container.release_damaged_bikes_to(self.other_container)
        self.assertEqual(self.bike_container.total_count(), 5)
        self.assertEqual(self.bike_container.damaged_count(), 0)
        self.assertEqual(self.bike_container.fixed_count(), 5)
        self.assertEqual(self.other_container.damaged_count(), 5)

unittest.main()