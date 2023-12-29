from objects import *
from random import randint

from random import randint


def main():
    n, m = 5, 5
    garden = Garden(n, m)
    plants = [("Flower", 3), ("Tree", 2), ("Bush", 2)]

    for plant_type, quantity in plants:
        for i in range(quantity):
            x, y = randint(0, n - 1), randint(0, n - 1)
            plant = globals()[plant_type](name=f'{plant_type.lower()}{i}')
            garden.add_plant(plant, x, y)

    garden.show()


def simulation():
    garden = Garden(5, 5)
    plant = Plant(name='plant1')
    garden.add_plant(plant, 2 - 1, 3 - 1)
    garden.show()
    while True:
        garden.end_day()
        garden.show()
        # break


if __name__ == '__main__':
    main()
    # simulation()
