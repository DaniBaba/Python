def invite(list):
    for i in list:
        print('Hey ' + i + '! you are invited for dinner')
    print()

def print_list(list):
    for i in list:
        print(i)
    print()

# 3.4
guestlist = ['Faizan', 'Waqas', 'Faraz']
invite(guestlist)

# 3.5
guestlist[0] = 'Arbaz'
invite(guestlist)

# 3.6
print('We found a bigger dinner table.')
guestlist.insert(0,'Sameer')
guestlist.insert(int(len(guestlist)/2), 'Rehan')
guestlist.append('Emad')
invite(guestlist)

# 3.7
print('Sorry for some issues but I can invite only two guests for dinner.\nThe name are given to of removed guest from list!')
while len(guestlist) > 2:
    print('Sorry ' + guestlist.pop() + "! You are not invited")
invite(guestlist)
del guestlist[-1]
del guestlist[-1]
print(len(guestlist))

# 3.8
location = ['Johor', 'Gulshan', 'Nepa', 'Waterpump', 'Malir', 'North']
print(location)
print(sorted(location))
print(location)
print(sorted(location, reverse=True))
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

# 3.9
guestlist = ['Waqas', 'Faraz']
print('The number of guests invited are ' + str(len(guestlist)))

# 3.10
languages = ['c#', 'java', ' python ', 'PHP', 'JavaScript', 'C++']
mylanguages = []
for i in languages[:4]:
    mylanguages.append(i)
print(mylanguages[0].title())
print(mylanguages[1].upper())
print(mylanguages[2].title().strip())
print(mylanguages[3].lower())
mylanguages.sort()
print(mylanguages)


# 4.10
datalist = ['hydrogen', 'oxygen', 'nitrogen', 'helium', 'benzene']
print('The first three items in list are : ' + str([i for i in datalist[:3]]))
print('The middle three items in list are : ' + str([i for i in datalist[int(len(datalist)/2-1.5):int(len(datalist)/2+1.5)]]))
print('The last three items in list are : ' + str([i for i in datalist[-3:]]))

# 4.11
pizzas = ['Hawaiian', 'Champagne Ham & Cheese', 'Beef & Onion', 'Pepperoni']
friends_pizzas = pizzas[:]
print("My pizzas are ")
print_list(pizzas)
print("My friend's pizzas are ")
print_list(friends_pizzas)
pizzas.append('Simply Cheese')
friends_pizzas.append('Italiano')
print("My included pizzas are ")
print_list(pizzas)
print("My friend's included pizzas are ")
print_list(friends_pizzas)

# 4.12
pizzas = ['Hawaiian', 'Champagne Ham & Cheese', 'Beef & Onion', 'Pepperoni']
foods = ['Biryani', 'Burger', 'Karahi', 'Handi']
print("Pizzas are : ")
print_list(pizzas)
print("Foods are : ")
print_list(foods)

# 4.13
foods = ('Biryani', 'Burger', 'Karahi', 'Handi', 'Korma')
for i in foods:
    print(i)
# foods[0] = 'Chowmen'        #Shows Error because tuple can't modified
foods = ('Biryani', 'Sajji', 'Karahi', 'Handi', 'Chowmen')
for i in foods:
    print(i)


# Project Euler - Problem 2
def fiboancci(range_input):
    num1 = 0
    num2 = 1
    num3 = 0
    sum_of_even = 0
    for i in range(2,range_input):
        num3 = num1 + num2
        if sum_of_even > range_input:
            print(sum_of_even)
            return
        if num3 % 2 == 0:
            sum_of_even += num3
        num1 = num2
        num2 = num3

fiboancci(4000000)