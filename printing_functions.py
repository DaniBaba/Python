def print_models():
    print('Model is printed')

def factors(number):
    array = []
    for i in range(2,number):
        if number%i == 0:
            array.append(i)
    print(array)