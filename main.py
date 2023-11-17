from objects import *


def main():
    garden = Garden(3, 3)
    plant = Plant(name='test')
    garden.add_plant(plant, 0, 0)
    tree = Tree(name='tree')
    print(tree.name, tree.emoji)


if __name__ == '__main__':
    main()
