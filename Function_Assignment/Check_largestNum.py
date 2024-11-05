def checklarge(Number1,Number2):
    if(Number1>Number2):
            print(Number1," is the largest number")
    else:
            print(Number2,"is the not largest number")
    
   

def main():

    print('enter the Number:')
    Number1 = int(input())
    print('enter the Number:')
    Number2 = int(input())
    checklarge(Number1,Number2)
        

if __name__=="__main__":
    main()


