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
    print('Enter the values:')
    for i in range(size):
        value = int(input())
        lst.append(value)

    print('User List:', lst)
    greterthen_number = list(filter(checknumber,lst))
    print('Greater than number:', greterthen_number)

    maplist = tuple(map(lambda number: number - 10, greterthen_number))
    print('Mapped List:', maplist)

    reduce_list = reduce(lambda number1, number2: number1*number2,maplist)
    print('multiplication List:',reduce_list)   

if __name__ == "__main__":
    main()

