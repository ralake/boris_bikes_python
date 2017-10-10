class BikeContainer:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.bikes = []

    def dock(self, bike):
        self.bikes.append(bike)

    def release(self, bike):
        self.bikes.remove(bike)

    def total_count(self):
        return len(self.bikes)

    def fixed_count(self):
        return len(self.__get_bikes())

    def damaged_count(self):
        return len(self.__get_bikes(True))       

    def is_full(self):
        return self.total_count() == self.capacity

    def is_empty(self):
        return self.total_count() == 0

    def release_fixed_bikes_to(self, bike_container):
        self.__move_bikes(bike_container)

    def release_damaged_bikes_to(self, bike_container):
        self.__move_bikes(bike_container, True)

    def __get_bikes(self, is_damaged = False):
        return [bike for bike in self.bikes if bike.is_damaged == is_damaged]

    def __move_bikes(self, bike_container, is_damaged = False):
        bikes = self.__get_bikes(is_damaged)
        for bike in bikes:
            self.release(bike)
            bike_container.dock(bike)


