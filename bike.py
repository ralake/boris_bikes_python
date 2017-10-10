class Bike:
    def __init__(self):
        self.is_damaged = False
  
    def fix(self):
        self.is_damaged = False

    def damage(self):
        self.is_damaged = True