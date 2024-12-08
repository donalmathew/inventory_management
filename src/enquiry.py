from data import inventory

#print(data.inventory["000"]["items"]["000"]["name"])


def enquiry():
    id_num=input("enter id num\n")
    item_name=inventory[id_num[:3]]["items"][id_num[3:6]]["name"]
    item_price=inventory[id_num[:3]]["items"][id_num[3:6]]["price"]
    item_color_available=inventory[id_num[:3]]["items"][id_num[3:6]]["color"]
    
    #print(inventory[id_num[:3]]["items"][id_num[3:6]]["color"][id_num[6:8]]["quantity"])
    total_quantity=0
    for key in item_color_available:
        total_quantity+=int(item_color_available[key]["quantity"])
            

    if total_quantity==0:
        print()
        print("item not available")
        print()
    else:
        print("________________________")
        print("item name:",item_name)
        print("price:",item_price)
        print()
        print("available: ",total_quantity," nos")
        print()
        print("colors available:")

        for key in item_color_available:
            for value in item_color_available[key].values():
                print(value," ",end='')
            print()

        print("________________________\n")