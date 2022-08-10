class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': N' + str(self.price)

    def get_total_price(self, count):
        total_price = count * self.price

        if count >= 3:
            total_price *= 0.9

        return round(total_price)
