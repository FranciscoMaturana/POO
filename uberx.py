from car import Car

class uberx(Car):
    brand = str
    model = str

    def __init__(self,license, driver, brand, model):
        super.__init__(license)
        self.brand = brand
        self.model = model