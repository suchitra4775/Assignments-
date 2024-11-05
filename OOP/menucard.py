class Menucard:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.menu = []

    def Accept(self):
        print('Enter the number of item you want to add')
        self.size = int(input())
        for i in range(self.size):
            print("Enter the Details",i+1)
            name = input("Enter the Name:")
            price = float(input("Enter the price:"))
            self.add(name,price)
    
    def add(self,name,price):
        item = (f"Name : {name}, price: {price}")  
        self.menu.append(item)

    def display(self):
        print('********Menu*******')
        if len(self.menu) == 0:
            print("The Menu is blank")
        else:   
            for item in self.menu:
                print(item)  
   
def main():
    Obj1 = Menucard("mango",145)
    Obj1.Accept()
    Obj1.display()

if __name__=="__main__":
   main()
        

