from objects import *
from random import randint
import pickle

def main(preset=True):
    if preset:
        n, m = 5, 5
        garden = Garden(n, m)
        plants = [("Flower", 3), ("Tree", 2), ("Bush", 2)]

        for plant_type, quantity in plants:
            for i in range(quantity):
                x, y = randint(0, n - 1), randint(0, n - 1)
                plant = globals()[plant_type](name=f'{plant_type.lower()}{i}')
                garden.add_plant(plant, x, y)
    else:
        with open('garden.pkl', 'rb') as file:
            garden = pickle.load(file)


    while True:
        garden.show()
        print("Choose an action:")
        print("1. Add more plants")
        print("2. Water them")
        print("3. Harvest")
        print("4. Skip day")
        print("5. Status")
        print("6. Exit")
        print("7. Save garden to file")
        choice = input("Enter your choice (1-7): ")

        #  TODO maybe do it in switch case
        if choice == '1':
            coords = input("Enter coordinates x,y (leave blank if random): ")
            x,y=map(int, coords.split(',')) if coords else (randint(0, n - 1), randint(0, n - 1))

            plant_type = ''
            while plant_type not in {"Flower", "Tree", "Bush"}: 
                plant_type = input("Enter plant type (Flower, Tree, Bush): ")
                if plant_type not in {"Flower", "Tree", "Bush"}:
                    print("Invalid plant type. Please enter a valid plant type.")
            
            name = input("Enter plant name: ") or f'{plant_type.lower()}{randint(0, 100)}'
            plant = globals()[plant_type](name=name)  # Ensure globals()[plant_type] is safe to use
            garden.add_plant(plant, x, y)

        elif choice == '2':
            garden.water_plant()
        elif choice == '3':
            garden.harvest_plant()
        elif choice == '4':
            garden.end_day()
        elif choice == '5':
            status = garden.status()
            for plant in status:
                print("-"*30)  # Divider between plants
                print(f"{plant['name']} {plant['emoji']} - Lvl: {plant['level']} - Coord: {plant['coordinates']}")
                print("Req: ", end='')
                print(" ".join([f"{key.split('_')[0]}:{value}" for key, value in plant['requirements'].items()]))
                print("Care: ", end='')
                print(" ".join([f"{key.split('_')[0]}:{value}" for key, value in plant['care_record'].items()]))
            print("-"*30)  # Divider between plants
        elif choice == '6':
            break
        elif choice == '7':
            filename = 'garden.pkl'
            with open(filename, 'wb') as file:
                pickle.dump(garden, file)
            print(f"Garden saved to {filename}.")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main(True)
