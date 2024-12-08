from enquiry import enquiry
from menu import menu


#main functioin
flag=0
while(flag==0):
    print()
    print("____________  Enter:     bill new item  ____________")
    print("________________  9:     menu  _____________________")
    print("________________  0:     exit application  _________")
    n=input("")

    match n:
        case "9":
            menu()
        case "0":
            flag=1
        case _:
            enquiry()


