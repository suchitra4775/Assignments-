class Demo:
    value = 0
    
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")

    def Gun(self):
        print(f"Value of no1: {self.no1}")
        print(f"Value of no2: {self.no2}")

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    print("Object 1:")
    Obj1.Fun()
    Obj1.Gun()
    print()
    print("Object 2:")
    Obj2.Fun()
    Obj2.Gun()
    
if __name__=="__main__":
    main()