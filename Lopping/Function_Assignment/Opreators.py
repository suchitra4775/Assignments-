def add(value1,value2):
    ans = value1+value2
    return ans
def sub(value_3,value_4):
    ans = value_3-value_4
    return ans
def mul(value5,value6):
    ans = value5*value6
    return ans
def div(value7,value8):
    ans = value7/value8
    return ans
def floordivision(value9,value10):
    ans = value9//value10
    return ans
def Modulus(value11,value12):
    ans = value11%value12
    return ans
def power(value13,value14):
    ans = value13**value14
    return ansel

def main():
    print('Choose operator(+)(-)(*)(/)(//)(%)(**)')
    selct = int(input())
    print('Enter first number:')
    value_1 = int(input())
    print('Enter second number:')
    value_2 = int(input())
    if(selct==1):
        Output_1 = add(value_1,value_2) 
        print('Addition:',Output_1)
    elif(selct==2):
        Output_2 = sub(value_1,value_2)
        print('subtraction:',Output_2)
    elif(selct==3):
        Output_2 = mul(value_1,value_2)
        print('multiplication:',Output_2)
    elif(selct==4):
        Output_4 = div(value_1,value_2)
        print('division:',Output_4)
    elif(selct==5):
        Output_5 = floordivision(value_1,value_2)
        print('floor division:',Output_5)
    elif(selct==6):
        Output_6 = Modulus(value_1,value_2)
        print('Modulus:',Output_6)
    elif(selct==7):
        output_7 = power(value_1,value_2)
        print('power:',output_7)
    else:
        print("please select add,sub,mul,div ")
if __name__=="__main__":
    main()