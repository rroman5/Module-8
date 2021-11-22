#Roberto Roman
#11-16-2021

#Problem 1
#This Problem will take two inputs given from the user and print wether they are equal or not.
x = int(input("Insert number "))
y = int(input("Insert another number "))
def equal(num1,num2):
        if int(num1) == int(num2):
                print("Numbers are equal")
        else:
                print("Not equal")
equal(x,y)

#Problem 2
#This problem we will write a function that takes two inputs from a user and prints whether the sum is greater than 10,
#less than 10, or equal to 1

def greater_equal_less (num1,num2):
        sum = num1 + num2
        if sum > 10:
                print("Is greater then 10")
        elif sum < 10:
                print("Is less than 10")
        else:
                print("Is equal ")

greater_equal_less(x,y)

#Problem 3
# – Write a function that takes a list and prints if the value 5 is in that list.
z = [5,7,10,2,]
def get_list(list):
        if 5 in list:
                print("5 is the list")
        else:
                print("5 is not in the list ")
#Problem 4
#Write a function that takes a year as a parameter and returns True if the year is a
#leap year, False if it is otherwise.
#Consider the requirements of a leap year:
#The year is evenly divisible by 4
#If the year can be evenly divided by 100 it is NOT a leap year, unless:
#oIf the year is also evenly divisible by 400, then it is a leap year.
def leaper(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0):

      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):

      leap = True
  else:
      leap = False

  return leap

year = int(input("Insert year"))
print(leaper(year))



