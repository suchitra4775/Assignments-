import os
def count_string_frequency():
    file_name = input("Enter the file name: ")

        with open(file_name, 'r') as file:
            contents = file.read()

        frequency = contents.count(search_string)

        print(f"The string '{search_string}' occurs {frequency} times in '{file_name}'.")


def main():

    count_string_frequency()

if __name__=="__main__":
    main()