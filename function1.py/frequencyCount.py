#String formating => the process of inserting custom string 
#or variable in a predefined text. =>f"{}"
def count_num(lst,num):
    count = 0
    for number in lst:
        if(num==number):
            count = count + 1
    return count        


def main():
    input_list = []
    size = int(input("Enter the size of list: "))
    print("enter the value:")
    for i in range(size):
        values = int(input())
        input_list.append(values)
    print("input data list = ",input_list) 

    num = int(input("enter the number to find its frequency"))
    output = count_num(input_list,num)
    print(f"{num} is repected {output} times")

if __name__=="__main__":
    main()