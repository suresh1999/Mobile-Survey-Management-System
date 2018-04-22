import pickle
from mobile import Mobile, get, FILE_NAME

def modify():
    mod_no = input("Enter the model number:")
    mobile = get("MX" + mod_no)
    if mobile:
        data = {}
        data['name'] = input("Enter the model name :")
        data['price'] = int(input("Enter the price:"))
        data['year'] = input("Enter the Year:")
        data['sold'] = int(input("Enter the number of items sold:"))
        data['rating'] = float(input("Enter the rating:"))
        mob = Mobile(number=mod_no, **data)
        prev = []
        with open(FILE_NAME,"rb") as fp:
            prev = pickle.load(fp)
        for i in range(len(prev)):
            if prev[i].getNumber() == mob.getNumber():
                prev[i] = mob
        with open(FILE_NAME, "wb") as fp:
            pickle.dump(prev, fp)
        print("Successfully modified details of "+ mob.getNumber())
    else:
        print("No mobile exists with the model number "+mod_no)
