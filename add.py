import pickle
from mobile import Mobile, NameException, NumberException, NegativeException,MobileExists, YearException

def addMobile():
    data = {}
    
    data['name'] = input("Enter the model name :")
    data['number'] = input("Enter the model number :")
    data['price'] = int(input("Enter the price:"))
    data['year'] = input("Enter the Year")
    data['sold'] = int(input("Enter the number of items sold:"))
    data['rating'] = float(input("Enter the rating"))
    mob = None
    try:
        mob = Mobile(**data)
    except (NameException,NumberException,NegativeException,YearException) as e:
        print(e.msg)
    else:
        try:
            mob.save()
        except MobileExists:
            print("Already an mobile exists with the model number " + mob.getNumber())
        else:
            print("Mobile successfully created")