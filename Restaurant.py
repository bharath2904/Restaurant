import time

def welcome():
    print("Welcome to our BURGER and DRINKS")
    print("Take your Order here")
    burger()
    
def burger():
    burger_list=["veg","non veg"]
    print(burger_list)
    request=input("Please enter your burger (veg/non veg) :")
    if request == "veg":
       print(request," are Available")
       veg()
    elif request == "non veg":
        print(request,"are available")
        non_veg()
    else:
       print("Processing...")
       time.sleep(1)
       print(request,",Sorry not Available")
       welcome()
def veg():
    veg_list=["paneer","cheese","chinese","vegetables","healthy","pav bhaji"]
    choice=input("Choose your veg burger:")
    print(veg_list)
    if choice in veg_list:
        print(choice," are available here")
        obj=order()
        obj.pay()
        soft_drinks()
    else:
        print(choice,"is not available please choose above menu")
        print(veg_list)
        
class order():
    def pay(self):
        
        size=["Regular","Large","Special"]
        print(size)
        select=input("Choose your Category:")
        if select in size:
            print("Add to order")
    def book(self):
        print("Pay at counter\n"
              "Mobile Payment")

def non_veg():
    nonveg_list=["chicken","mutton","friedchicken","beef"]
    choose=input("Choose your non-veg burger:")
    print(nonveg_list)
    if choose in nonveg_list:
        print(choose,"are available here")
        obj=order()
        obj.pay()
        soft_drinks()
        
    
    else:   
        print(choose,"is not available please choose above menu")
        print(nonveg_list)
       
def soft_drinks():
    drinks=["Coke","sprite","icedcoke","icecream","hottea","hotchocolate"]
    print(drinks)
    request=input("Please enter your drinks :")
    if request in drinks:
        print(request," are Available")
        obj=order()
        obj.book()
        thanks()
       
    else:
        print("Processing...")
        time.sleep(1)
        print(request,",Sorry is not currently Available")

def thanks():
    print("Enjoy your day!!! and Most Welcome")

welcome()