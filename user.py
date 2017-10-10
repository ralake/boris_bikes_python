class User:
    def __init__(self, bike = None):
        self.bike = bike

    def damage_bike(self):
        if self.bike:
            self.bike.damage()

    def lose_bike(self):
        self.__remove_bike()

    def __remove_bike(self):
        self.bike = None