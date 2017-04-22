
#--------------------------------------------------------------------------------------------------
#Excercise : 8-3

def make_shirt(size, msg):
    print("The Size of the Shirt is " + size + ', & the text for a shirt "' + msg + '"')

make_shirt('medium', "I am best")             #positional argument
make_shirt(msg="I am best", size='small')          #keyword argument

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-4

def make_shirt(size='large', msg='I love python'):
    print("The Size of the Shirt is " + size + ', & the text for a shirt "' + msg + '"')

make_shirt()
make_shirt('medium')
make_shirt('small','No buddy is perfect I am No Buddy')

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-5

def describe_city(city, country='Pakistan'):
    print(city.title() + ' is in ' + country.title())

describe_city('karachi')
describe_city('Lahore')
describe_city('Dehli', 'India')

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-12

def make_sandwich(*items):
    print('\nList of your ordered sandwiches :-\n')
    for i in items:
        print('your order : ' + i)
    print('Your order is ready.')

make_sandwich('Triple Decker California Club', 'Tempeh Reuben Club Sandwich', 'Mediterranean Veggie Sandwich')
make_sandwich('Leftover Turkey Salad Sandwich', 'Chickpea Salad Sandwich', 'Greek Chicken Salad Pita Tacos')
make_sandwich('Buffalo Tempeh and Kale Wraps', 'Roasted Cauliflower and Spicy Tofu Wraps', 'Strawberry Balsamic Chicken Wrap')

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-13

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)

build_profile('Daniyal', 'Saleem', location='Pakistan', field='Computer')

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-14

def make_car(car,model, **spec):
    array = {}
    array['car'] = car
    array['model'] = model
    for k,v in spec.items():
        array[k] = v
    print(array)

make_car('Mercedes', '2017', color='Black', type='imported')

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-15

import printing_functions
printing_functions.print_models()

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-16

import printing_functions
from printing_functions import print_models
from printing_functions import print_models as pm
import printing_functions as pf
from printing_functions import *

print_models()
pm()
pf.print_models()

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Excercise : 8-17

#----Program 1

def factorials(number):
    result = str(number) + ' = ';
    while number > 0:
        if number > 1:
            result += str(number) + ' X '
        else:
            result += str(number)
        number = number - 1
    print(result)

factorials(3)


#----Program 2

import printing_functions as pf
pf.factors(50)


#----Program 3

def print_list(list):
    count = 1
    for i in list:
        print(str(count) + ') ' + i.title())
        count = count + 1

def about_university():
    university = {'about fields': ['bscs', 'bba', 'hr'], 'about teachers': ['teachers are highly qualified', 'sincere about work'],
              'about students': ['students are very talented', 'get highest gpa', 'respect their teachers']}

    print('PRESTON UNIVERSITY')
    for k,v in university.items():
        print('\n'+ k.upper() + ': \n')
        print_list(v)

about_university()

#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
#Project Euler : Problem # 3

def largest_prime_factor(number):
    given_number = number
    count = 1
    a = 2
    factors = []
    while a <= number:
        while number%a == 0:
            number = number /  a
            factors.append(a)
        a = a + 1
    print('The largest prime factor of given number ' + str(given_number) + ' are = ' +  str(factors))

largest_prime_factor(600851475143)

#--------------------------------------------------------------------------------------------------