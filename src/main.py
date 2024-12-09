from enquiry import enquiry
from menu import menu
from clear_screen import clear_screen
from bill import bill



#main functioin
def main():
    clear_screen()

    flag=0
    while(flag==0):
        print()
        print("____________________Welcome_________________________")
        print()
        print("____________  Enter:     bill new item  ____________")
        print("________________  9:     menu  _____________________")
        print("________________  0:     exit application  _________")
        #input
        print()
        n=input("Enter selection: ")
        print()

        clear_screen()

        match n:
            case "9":
                menu()
                clear_screen()
            case "0":
                flag=1
            case _:
                bill()
                #to clear screen when function returns
                clear_screen()


main()