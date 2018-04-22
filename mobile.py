
import pickle

FILE_NAME = "mobile.dbs"
class NameException(Exception):
    def __init__(self):
        self.msg = "Model name should be maximum of 15 characters"

class NumberException(Exception):
    def __init__(self):
        self.msg = "Model number should be a 8 digit number"

class YearException(Exception):
    def __init__(self):
        self.msg = "Year should 4 digit number"

class NegativeException(Exception):
    def __init__(self, field):
        self.msg = "Negative values are not allowed for " + field

class MobileExists(Exception):
    pass

class Mobile(object):

    def __init__(self, name, number, year, price, rating, sold):
        self.setName(name)
        self.setNumber(number)
        self.setYear(year)
        self.setPrice(price)
        self.setRating(rating)
        self.setProductSold(sold)

    def setName(self, name):
        if len(name) > 15:
            raise YearException
        else:
            self.__name = name
    
    def setNumber(self, no):
        if len(no) == 8 and no.isdigit():
            self.__number = "MX" + no
        else:
            raise NumberException
            
    def getNumber(self):
        return self.__number
    def setYear(self, no):
        if len(no) == 4 and no.isdigit():
            self.__year = no
        else:
            raise YearException

    def setPrice(self, price):
        if price > -1:
            self.__price = price
        else:
            raise NegativeException("Price")
    
    def setRating(self, rate):
        if rate > -1:
            self.__rating = rate
        else:
            raise NegativeException("Rating")

    def setProductSold(self, count):
        if count > -1:
            self.__sold = count
        else:
            raise NegativeException("Product sold")

    def __str__(self):
        return self.__number
        
    def display(self):
        print("Models Name : "+ self.__name)
        print("Model Number : " + self.__number)
        print("Year : " , self.__year)
        print("Price : " , self.__price)
        print("Rating : " , self.__rating)

    def save(self):
        prev = []
        with open(FILE_NAME,'rb') as fp:
            prev = pickle.load(fp)
            for i in prev:
                if i.__number == self.__number:
                    raise MobileExists
            prev.append(self)
        with open(FILE_NAME,'wb') as fp:
            pickle.dump(prev, fp)

def get(modelno):
        with open(FILE_NAME,'rb') as fp:
            prev = pickle.load(fp)
            for mob in prev :
                if mob.getNumber() == modelno:
                    return mob
        return None
# if __name__ == "__main__":


#     with open(FILE_NAME, "rb") as fp:
#         a = pickle.load(fp)
#         for i in a:
#             print(i)

#     print('\n')
#     print(Mobile.get('MX45612341'))

    