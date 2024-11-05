def CheckEven():

    print('enter the number:')
    number = int(input())
    if(number%2==0):
        print('Even number')
    else:
        print('odd number')


def main():
    #user and function call inside main()
    CheckEven()
if __name__=="__main__":
    main() #main functioncall


# >>> print(__name__)
# __main__
# >>>

