import weakref
from memory_profiler import profile


class Car:
    list_of_cars = []

    def new_car(self, x):
        self.list_of_cars.append(x)


class WeakCar:
    list_of_cars = []

    def new_car(self, x):
        self.list_of_cars.append(weakref.ref(x))


class CarSlots:
    __slots__ = ("x")

    list_of_cars = []

    def new_car(self, x):
        self.list_of_cars.append(x)


@profile
def creating_instances(n):
    cars = [Car() for i in range(n)]
    return cars


@profile
def creating_weak_instances(n):
    weak_cars = [WeakCar() for i in range(n)]
    return weak_cars


@profile
def creating_slots_instances(n):
    slots_cars = [CarSlots() for i in range(n)]
    return slots_cars


# @profile
# def changing_attributes(m):
#     new_cars = [Car() for i in range(m)]


if __name__ == "__main__":
    n = 50_000
    creating_instances(n)
    creating_weak_instances(n)
    creating_slots_instances(n)
    car = Car()
    print(car.__dict__)
