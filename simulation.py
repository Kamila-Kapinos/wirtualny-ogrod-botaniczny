from objects import *


def simulation():
    garden = Garden(5, 5)
    garden.add_plant(Plant(name='plant1'), 2 - 1, 3 - 1)
    garden.show()
    while True:
        garden.end_day()
        garden.show()
        # break


if __name__ == '__main__':
    simulation()
