from hey import MenuItem


class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        return self.name + ': N' + str(self.price) + ' (' + str(self.volume) + 'mL)'
