def course(replace):
    return replace

def main():
    course = ['', 'Python', 'java', ',,', 'angul:ar', 'php']

    cleaned_course = [item.replace(':', '').replace(',', '') for item in course if item not in ['', ',,']]
    final_course = [item.lower() for item in cleaned_course if item in ['Python', 'java', 'php']]
    print(final_course)


if __name__=="__main__":
    main()

