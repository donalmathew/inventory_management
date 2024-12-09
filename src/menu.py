from enquiry import enquiry
from clear_screen import clear_screen

def menu():
    print("______________________MENU_________________________")
    print()
    print("________________  1:     add new item  ____________")
    print("________________  2:     delete an item  __________")
    print("________________  3:     enquiry  _________________")

    print()
    m=input("Enter selection: ")
    print()
    
    clear_screen()

    match(m):
        case "3":
            enquiry()