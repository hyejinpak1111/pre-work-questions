#Question1 
#Write a function to print "hello_USERNAME!" is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name + "!")
    
hello_name("juneun")


#Question2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():

def first_odds():
    for i in range(1,100,2):
        print(i)

first_odds()
#Question3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list)

def max_num_in_list(a_list):
    curr_highest = a_list[0]
    
    for i in a_list:
        if i > curr_highest:
            curr_highest = i
            
    return curr_highest

print (max_num_in_list([50,49,90,10,34]))

#Question4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
print (is_leap_year(400)) #True
print (is_leap_year(2012)) #True
print (is_leap_year(2000)) #True
print (is_leap_year(2100)) #False
print (is_leap_year(2001)) #False


#Question5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    diff = a_list[0] - 0
    
    for idx, val in enumerate(a_list):
        if val - idx != diff:
            return False
        
    return True
    
print(is_consecutive([1,2,3,4]))