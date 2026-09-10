
# Lab Class 

print("1-------------------------------------------------------\n")
my_dict = { "Tom":"tom123@gmail.com" ,"Bill":"gates678@gmail.com"}

# To get a value from a Key 
print(my_dict["Tom"])

for x,y in my_dict.items():
    print(x,"-",y)
    
    
print("2-------------------------------------------------------\n")

# Built in methods for string formatting
Sales_record_dict ={
    "price": 6.8 ,
    "Total_items": 10 ,
    "Name": "Tom" 
    
}

print(f"Tom bought total",Sales_record_dict["Total_items"],"items with",Sales_record_dict["price"], 
      "and total price=",Sales_record_dict["price"]*Sales_record_dict["Total_items"])


#print(Sales_record_dict.format())

# Time 
print("3-------------------------------------------------------\n")
from datetime import date,timedelta
from datetime import time
from datetime import datetime

today = date.today()
print("Present Date is -- ",today)

dt_time_now = datetime.today()
print("date time--",dt_time_now)

#from datetime import date, timedelta

specific_date = date.today() + timedelta(days=120)
print(specific_date)

print("4-------------------------------------------------------\n")

# Class in Python

class Person:
    institute = "MSIS"
    
    def set_name(self, new_name):
        self.name=new_name
        
    def set_location(self,new_location):
        self.location = new_location
    
    def print_details(self):
        print(self.name , self.location)
        
ob_person = Person()
ob_person.set_name("Tom")
ob_person.set_location("Manipal, Karnataka")
ob_person.print_details()
print("5-------------------------------------------------------\n")

# Sets are unordered 
x= ("one" , 2 , True ,2.22)
y=( "two" , "xr" , "ur" , False , 45.5)

print(x,y)

print("6-------------------------------------------------------\n")
# map()

def calculateSquare(n):
    return n * n

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

result = map(calculateSquare, numbers)

print(list(result))

res = map(lambda x: x*x , numbers)
print(list(res))

num1 = [ 1,2,3,4,5,6]
num2= [7,8,9,10,11,12]
res = map(lambda n1,n2: n1*n2 , num1 ,num2)
print(list(res))



print("-------------------------------------------------------\n")

# Assignment 
print("1-------------------------------------------------------\n")
 #1 to print Odd numbers 
for i in range(200):
    if i%2 == 1:
        print(i," ",end="")