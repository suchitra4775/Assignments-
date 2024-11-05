def word(remove):
     return remove
# This function is defined but not used in the program. It takes a parameter remove and simply returns it. 
# Since it isn't called anywhere, it doesn't affect the output.


# lst is a list of strings containing elements that have a format of "WORD-NUMBER" (e.g., 'HEM-234').
def main():
  
    lst = ['HEM-234','HML-123','HELLO-99']# split method 
    cleaned_lst = [item.split('-')[0] for item in lst]

    
    print(cleaned_lst)


    # For each item, it splits the string at the hyphen (-) using item.split('-'), which creates a list of two elements: 
    # the part before the hyphen and the part after it.
    # [0] accesses the first element of this list, which is the part before the hyphen.
    # The result is a new list cleaned_lst, which will contain just the words from the original list, without the numbers.


if __name__ == "__main__":
    main()


