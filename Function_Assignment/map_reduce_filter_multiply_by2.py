from functools import reduce
def checkEven(Number):
    if  (Number%2==0):
       return True
    return False

def multiply_by_two(num):
    return num * 2

def find_max(num1,num2):
    return max(num1,num2)

def main():
    size = int(input('Enter the Size:'))
    lst = []
    print('Enter the values:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:', lst)

    Even_number = list(filter(checkEven,lst))
    print('Even Number:',Even_number)

    mapped_numbers = list(map(multiply_by_two, Even_number))
    print('Numbers after multiplying by 2:',mapped_numbers)

    max_number = reduce(find_max, mapped_numbers)
    print('Maximum number after processing:',max_number)

if __name__ == "__main__":
    main()
