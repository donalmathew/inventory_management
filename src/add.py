#importing as json
import json
file_path="../data/inventory.json"
with open(file_path, "r") as file:
    inventory = json.load(file)


def add():

    flag=1
    while(flag):
        print()
        print("1: add new class")
        print("2: add new item")
        print("3: increment item quantity")
        print("0: return to menu")
        print()

        a=input("enter input here: ")

        if a=="1":
            new_class()
        # elif a=="2":
        #     new_item()
        # elif a=="3":
        #     inc_quant()
        else:
            flag=0


def new_class():

    last_key=list(inventory.keys())[-1]
    new_key=str(int(last_key)+1).zfill(3)

    print()
    name=input("enter class name: ")

    inventory[new_key] = {
        "name": name,
        "items": {}  # Initialize with empty items
    }

    #writing to json file
    with open(file_path, "w") as file:
        json.dump(inventory, file, indent=4)
    
    print()
    print("class added successfully....")
    input("<-- return to menu? ")