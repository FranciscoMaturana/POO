from car import Car
from account import Account
from payment import Payment
from route import Route

if __name__ =='__main__':
    print("Hello world")
    '''
    car = Car()
    car.license = "AMS123"
    car.driver = "Andrés Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "JKD423"
    car2.driver = "Grorge Dam"
    print(vars(car2))'''
    car = Car("AMS123", Account("Andrés Herrera", "39447128-4"))
    print(vars(car))
    print(vars(car.driver))