from enquiry import enquiry

def menu():
    print("________________  1:     add new item  ____________")
    print("________________  2:     delete an item  __________")
    print("________________  3:     enquiry  _________________")

    m=input()
    match(m):
        case "3":
            enquiry()