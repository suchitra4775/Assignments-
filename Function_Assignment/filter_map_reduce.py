from functools import reduce
def checknumber(number):
    if (number>=70 and number<=90):
        return True
    return False
    
def multiplication(number1,number2):
    return number1*number2

def decrement(number):
    return number - 10

def main():
    size = int(input('Enter the Size:'))
    lst = []
    print('enter the value:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:',lst)

    greterthen_number = tuple(filter (checknumber,lst))
    print('greterthen number:',greterthen_number)

    maplist = tuple(map(decrement,greterthen_number))
    print('map List:',maplist) 
    
    reduce_list = reduce(multiplication,maplist)
    print('multiplication List:',reduce_list)   



if __name__=="__main__":
    main()

