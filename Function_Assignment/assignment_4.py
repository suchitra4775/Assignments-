def CheckNum(Number):
    count_num(list,num)
    count = 0
    for number in list:
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


if __name__=="__main__":
    main()

