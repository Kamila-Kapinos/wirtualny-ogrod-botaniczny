from objects import *
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

    while True:
        garden.show()
        print("Choose an action:")
        print("1. Add more plants")
        print("2. Water them")
        print("3. Harvest")
        print("4. Skip day")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            plant_type = input("Enter plant type (Flower, Tree, Bush): ")
            for i in range(1):  # Assuming adding one plant at a time
                x, y = randint(0, n - 1), randint(0, n - 1)
                plant = globals()[plant_type](name=f'{plant_type.lower()}{randint(0, 100)}')
                garden.add_plant(plant, x, y)
        elif choice == '2':
            garden.water_plant()
        elif choice == '3':
            garden.harvest_plant()
        elif choice == '4':
            garden.end_day()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()