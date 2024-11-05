class BookStore:
    NoOfBooks = 0
    
    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1
    
    def Display(self):
        print(f"Name: {self.Name} Author:{self.Author} bookstore{BookStore.NoOfBooks}")


def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display() 

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display() 
    
if __name__=="__main__":
    main()



