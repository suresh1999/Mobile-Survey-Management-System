from mobile import Mobile,get
import pickle
def search():
    while True:
        mod_no = input("Enter the model no:")
        mob = get("MX"+mod_no)
        if mob:
            mob.display()
        else:
            print("No match for model no " + mod_no)
        choice = int(input("Press 1 or 2 to continue or break your search"))
        if choice == 2:
            break
    