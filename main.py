from objects import *
from random import randint


def main():
    n,m = 5,5
    garden = Garden(n, m)
    for i in range(n):
        x, y = randint(0, n-1), randint(0, n-1)
        plant = Flower(name=f'plant{i}')
        garden.add_plant(plant, x, y)
    for i in range(2):
        x, y = randint(0, n-1), randint(0, n-1)
        plant = Tree(name=f'plant{i}')
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
        #break


if __name__ == '__main__':
    main()
    #simulation()