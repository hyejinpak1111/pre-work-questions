#Question1 
#Write a function to print "hello_USERNAME!" is the input of the function. The first line of the code has been defined as below.
def print_username (input):
    user_name = 'hello_' + input.upper()
    print (user_name) #print statement

print_username('hyejinpak1111!')


#Question2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():

my_range = list(range(1, 100, 2))

print(my_range)

#Question3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list)

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
 
print(max_num_in_list([10, 50, 30, 60, 26, 70, 98]))

#Question4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    a_year = 2000

    if a_year % 400 == 0:
        return  True
    elif a_year % 100 != 0:
        return  False
    elif a_year % 4 == 0:
        return  True
    else:


#Question5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):