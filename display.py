import pickle
from mobile import FILE_NAME

def display():
    with open(FILE_NAME,'rb') as fp:
        mobiles = pickle.load(fp)
        for mobile in mobiles:
            mobile.display()
            print("\n")