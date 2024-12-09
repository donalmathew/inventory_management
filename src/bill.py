#importing from files from other folders
import sys
import os
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
sys.path.append(data_dir)
from data import inventory
#end importing files from other folders 

#other imports
from clear_screen import clear_screen



#global variable decalrations
bill_items={}
final_price=0
customer_contact_num=""


#--------------------------------------------------------------------------
#function starts
def bill():

    
    

    #adding items to bill
    flag=1
    while(flag==1):
        clear_screen()
        
        #bill item counter
        counter=1
        global bill_items

        #print the items in bill
        if bill_items!={}:
            total_amount=[]

            print("___________________________________________________")
            for key,value in bill_items.items():
 
                #printing name, price and quantity of the item
                #extracting name,price and quantuty from data:
                item_name=inventory[key[:3]]["items"][key[3:6]]["name"]
                item_price=inventory[key[:3]]["items"][key[3:6]]["price"]
                item_quantity=inventory[key[:3]]["items"][key[3:6]]["color"][key[6:]]["quantity"]
                item_color=inventory[key[:3]]["items"][key[3:6]]["color"][key[6:]]["color-name"]
                #printing name, price and quantity
                print(counter,"       ",item_name,"-",item_color,"       ",item_price,"      x",value)

                #total amount calculation
                total_amount.append((int(item_price))*int(value))
                global final_price
                final_price=sum(total_amount)
            print("                      total: ",final_price)
            print("___________________________________________________")


            #menu
            print()
            print()
            print("add another item: Enter")
            print("remove last item: 8")
            print("bill items: 1")
            #input
            print()
            m=input("Enter selection: ")
            print()
            #switch
            match(m):
                case "8":
                    bill_items.popitem()
                    total_amount.pop()
                    counter-=1
                    continue
                case "1":
                    flag=0
                case _:
                    flag=1

        #initial statement
        if(flag==1):
            id=input("enter product id: ")
            quantity=input("enter quantity: ")
            counter+=1

            bill_items[id]=quantity
            clear_screen()


    #--------------------------------------------------------------------------

    #displaying the bill to make sure to continue with it
    print("___________________________________________________")
    for key,value in bill_items.items():
        #printing name, price and quantity of the item
        #extracting name,price and quantuty from data:
        item_name=inventory[key[:3]]["items"][key[3:6]]["name"]
        item_price=inventory[key[:3]]["items"][key[3:6]]["price"]
        item_quantity=inventory[key[:3]]["items"][key[3:6]]["color"][key[6:]]["quantity"]
        #printing name, price and quantity
        print(counter,"       ",item_name,"-",item_color,"       ",item_price,"      x",value)
    print("                      total: ",final_price)
    print("___________________________________________________")
    
    #confirmation for printing and making cahnges to database
    print()
    print("1: Continue with the bill")
    print("0: Cancel and return")
    #input
    print()
    confirmation=input("Enter selection: ")
    print()
    #switch
    match(confirmation):
        case "1":
            customerDetails()
            dataChange()
            billFile()
            print("successfully billed")
        case "0":
            return



    #end message
    input("<-- go back?")



def customerDetails():
    print()
    global customer_contact_num
    customer_contact_num=input("Enter customer's contact number: ")
    #check for 10 digits, and put this in a loop to correct the number if typed wrongly

def dataChange():
    #extracting name,price and quantuty from data:
    for key,value in bill_items.items():
        global item_quantity
        item_quantity=inventory[key[:3]]["items"][key[3:6]]["color"][key[6:]]["quantity"]
        #changing values:
        item_quantity=str(int(item_quantity)-int(value))      



def billFile():
    import os

    # Define the relative path
    folder_path = '../bill_generated'
    file_name = customer_contact_num+".txt"
    file_path = os.path.join(folder_path, file_name)

    # Create the directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    #extract the necessary details
    


    # Write to the file
    with open(file_path, 'w') as file:
        file.write(f"{customer_contact_num}  : Customer Phone number")
        file.write("\n")
        file.write("___________________________________________________\n")
        counter=0
        for key,value in bill_items.items():
            counter+=1
            #printing name, price and quantity of the item
            #extracting name,price and quantuty from data:
            item_name=inventory[key[:3]]["items"][key[3:6]]["name"]
            item_price=inventory[key[:3]]["items"][key[3:6]]["price"]
            item_color=inventory[key[:3]]["items"][key[3:6]]["color"][key[6:]]["color-name"]
            #printing name, price and quantity
            file.write(f"{counter}       {item_name}-{item_color}       {item_price}      x{value}\n")
        file.write(f"                      total: {final_price}\n")
        file.write("___________________________________________________")        
