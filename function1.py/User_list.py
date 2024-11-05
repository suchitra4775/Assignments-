#Dynamic list creating - taking input values form user to crete list

def main():
    data_input = []
    size = int(input("enter the size of list: "))
    print("enter the value:")
    for i in range(size):
        values = int(input())
        data_input.append(values)
    print("input data list = ",data_input)

if __name__=="__main__":
    main()

