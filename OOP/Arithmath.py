class Arithmatics:
    def __init__(self,A,B):
        self.No1 = A    
        self.No2 = B

    def Add(self):
        return self.No1+self.No2
    
    def Sub(self):
        return self.No1-self.No2
    
    def Multi(self):
        return self.No1*self.No2
    
    def Div(self):
        return self.No1/self.No2
    
    
def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    obj = Arithmatics(value1,value2)

    Ans = obj.Add()
    print("Addition is: ",Ans)
    Ans1 = obj.Sub()
    print("Subtraction is: ",Ans1)
    Ans2 = obj.Multi()
    print("Multiplication is: ",Ans2)
    Ans3 = obj.Div()
    print("Division is: ",Ans3)


if __name__=="__main__":
    main()
        