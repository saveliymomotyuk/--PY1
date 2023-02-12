if __name__ == "__main__":
    # Write your solution here
    pass

class Auto:
    """класс - машина"""
    def __init__(self, carmark: str, drivespeed: int, seats: int, color: str):
        self.carmark = carmark
        self.drivespeed = drivespeed
        self.seats = seats
        self.color = color

    def __str__(self):
        return f"Машина Марки {self.carmark} едет со средней скоростью {self.drivespeed} и имеет {self.seats} мест для пассажиров, " \
               f"она {self.color} цвета."

    def __repr__(self):
        return f"{self.__class__.__name__}(carmark={self.carmark!r}, drivespeed={self.drivespeed!r})"

    def colorchange(self, newcolor): #метод реализующий перекраску автомобиля
        self.color = newcolor
        return newcolor

    def drive(self):
        print('Машина Едет')

    def stop(self):
        print('Машина стоит')


class LightAuto(Auto):
    """дочерний класс - Легковая машина"""
    def __init__(self, carmark: str, drivespeed: int, seats: int,color: str):
        super().__init__(carmark,drivespeed,seats,color)
        if isinstance(drivespeed, int):
            if drivespeed > 0:
                self.drivespeed = drivespeed
            else:
                raise AttributeError(f'speed cant be lower than 0')
        else:
            raise AttributeError(f'error - speed must be int')

    def drive(self):
        print('легковая машина Едет')

    def stop(self):
        print('легковая машина стоит')

    def __str__(self):
        return f"Легковая машина Марки {self.carmark} едет со средней скоростью {self.drivespeed} и имеет {self.seats} мест для пассажиров, " \
               f"она {self.color} цвета."



class HeavyAuto(Auto):
    """класс - Грузовая машина"""
    def __init__(self, carmark: str, drivespeed: int, seats: int, color: str):
        super().__init__(carmark, drivespeed, seats, color)

    def drive(self):
        print('Легковая машина стоит')

    def stop(self):
        print('Грузовая машина стоит')

    def __str__(self):
        return f"Грузовая машина Марки {self.carmark} едет со средней скоростью {self.drivespeed} и имеет {self.seats} мест для пассажиров, " \
               f"она {self.color} цвета."




car1 = Auto("Mercedes", 120, 4, "red")
print(car1)

car2 = LightAuto("Audi", 180, 2, "black")
print(car2)

car3 = HeavyAuto("Bus", 80, 20, "yellow")
print(car3)

car2.drive()
