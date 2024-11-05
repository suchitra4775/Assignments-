def Areaofcircle(Radius,PI=3.14)
    Result = PI*Radius*Radius
    return Result

def main():
    Rvalue = 10
    Pivalue = 3.14
    Output_1 = Areaofcircle(Radius,Pivalue)
    print('positinal Aregument:',Output_1)

it __name__=="__main__":
    main()