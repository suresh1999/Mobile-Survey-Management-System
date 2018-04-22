import os, pickle
import search
from add import addMobile
from display import display
from delete import delete
from modify import modify

FILE_NAME = 'mobile.dbs'

def init():
    if not os.path.isfile(FILE_NAME):
        data = []
        with open(FILE_NAME, 'wb') as fp:
            pickle.dump(data, fp, protocol=0)
            print(FILE_NAME + " created")


if __name__ == '__main__':
    init()
    while True:
        # os.system("clear")
        print("1.Add\n2.Delete\n3.Modify\n4.Search\n5.Display\n6.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            addMobile()
        elif choice == 2:
            delete()
        elif choice == 3:
            modify()
        elif choice == 4:
            search.search()
        elif choice == 5:
            display()
        else:
            break