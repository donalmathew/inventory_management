#importing from files from other folders
import sys
import os
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
sys.path.append(data_dir)
from data import inventory
#end importing files from other folders 

from clear_screen import clear_screen



#function starts
def bill():

    bill_items={}
    total_amount=0

    flag=1
    while(flag==1):
        clear_screen()
        
        #print the items in bill
        if bill_items!={}:
            total_amount=0

            print("___________________________________________________")
            for key,value in bill_items.items():
                print(key,": ",value)

                #total amount calculation
                total_amount+=int(value)
            print("                      total: ",total_amount)
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
                    continue
                case "1":
                    flag=0
                case _:
                    flag=1

        if(flag==1):
            id=input("enter product id: ")
            quantity=input("enter quantity: ")

            bill_items[id]=quantity
            clear_screen()


    #end message
    input("<-- go back?")



#delete this
#bill()