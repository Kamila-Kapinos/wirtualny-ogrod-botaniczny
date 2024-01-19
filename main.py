from objects import *
from random import randint
import pickle
import argparse

# branch
def main(garden_save):
    if garden_save:
        try:
            with open(garden_save, 'rb') as file:
                garden = pickle.load(file)
            print(f"Loaded garden from {garden_save}.")
        except Exception as e:
            print(f"Failed to load garden from {e}.")
    else:
        n = int(input("Enter garden size (n): "))
        m = int(input("Enter garden size (m): "))
        garden = Garden(n, m)
        
    
    # Show garden after loading/creation
    garden.show()

    while True:
        print("Choose an action:")
        print("1. Add more plants")
        print("2. Water them")
        print("3. Sunlight") # TODO: rename this?
        print("4. Harvest")
        print("5. End day")
        print("6. Status")
        
        
        print("9. Exit")
        print("0. Save garden to file")
        choice = input("Enter your choice (1-7): ")

        
        if choice == '1':
            coords = input("Enter coordinates y,x (leave blank if random): ")
            x,y=map(int, coords.split(',')) if coords else (randint(0, n - 1), randint(0, n - 1))
            
            # check if coords in range
            if x >= n or y >= m:
                print("Invalid coordinates. Please enter valid coordinates.")
                continue

            plant_type = ''
            while plant_type not in {"Flower", "Tree", "Bush"}: 
                plant_type = input("Enter plant type (Flower, Tree, Bush): ")
                if plant_type not in {"Flower", "Tree", "Bush"}:
                    print("Invalid plant type. Please enter a valid plant type.")
            
            name = input("Enter plant name: ") or f'{plant_type.lower()}{randint(0, 100)}'
            plant = globals()[plant_type](name=name)  # Ensure globals()[plant_type] is safe to use
            garden.add_plant(plant, x, y)

            # Add print after adding plant
            print(f"Added {plant_type} {name} at ({x},{y})")
            garden.show()

        elif choice == '2':
            input_coords = input("Enter coordinates x,y (leave blank for all): ")
            if input_coords:
                x,y=map(int, input_coords.split(','))
                garden.water_plant(x,y)
            else:
                garden.water_plant()

        elif choice == '3':
            input_coords = input("Enter coordinates x,y (leave blank for all): ")
            if input_coords:
                x,y=map(int, input_coords.split(','))
                garden.sunlight_plant(x,y)
            else:
                garden.sunlight_plant()

        elif choice == '4':
            input_coords = input("Enter coordinates x,y (leave blank for all): ")
            if input_coords:
                x,y=map(int, input_coords.split(','))
                harvested_fruits = garden.harvest_plant(x,y)
            else:
                harvested_fruits = garden.harvest_plant()
            print("Harvested fruits: ", [fruit._emoji for fruit in harvested_fruits])
                
        elif choice == '5':
            garden.end_day()
        elif choice == '6':
            status = garden.status()
            for plant in status:
                print("-"*30)  # Divider between plants
                print(f"{plant['name']} {plant['emoji']} - Lvl: {plant['level']} - Coord: {plant['coordinates']}")
                print("Req: ", end='')
                print(" ".join([f"{key.split('_')[0]}:{value}" for key, value in plant['requirements'].items()]))
                print("Care: ", end='')
                print(" ".join([f"{key.split('_')[0]}:{value}" for key, value in plant['care_record'].items()]))
                
                if 'fruitful' in plant:
                    print(
                        "Fruits:" , list(" ".join([f"{fruit._emoji}" for fruit in plant['fruit_list']]).split())
                    )

            print("-"*30)  # Divider between plants


            garden.show() # Show garden after status
        elif choice == '9':
            break
        elif choice == '0':
            filename = input("Enter filename to save to: ")
            with open(filename, 'wb') as file:
                pickle.dump(garden, file)
            print(f"Garden saved to {filename}.")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the garden program.")
    parser.add_argument('--seed', type=str, default=False,
                        help='Path to a garden pickle file to preload')
    
    args = parser.parse_args()
    main(args.seed)
