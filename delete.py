import pickle
from  mobile import FILE_NAME, get

def delete():
    mod_no = input("Enter the model number:")
    mobile = get("MX" + mod_no)
    if mobile:
        prev = []
        with open(FILE_NAME,"rb") as fp:
            prev = pickle.load(fp)
        prev = list(filter(lambda x: x.getNumber() != mobile.getNumber(),prev))
        with open(FILE_NAME, "wb") as fp:
            pickle.dump(prev, fp)
        print("Successfully Deleted")
    else:
        print("No mobile exists with the model number "+mod_no)

