def CheckNum(Number):


    if(Number%2==0):
        print(f"Even Number")
    else:
        print(f"odd Number")


def main():
    print('enter the Number:')
    Number = int(input())
    CheckNum(Number)


if __name__=="__main__":
    main() 


