def main():
    values = []
    value = input("Enter a value: ")
    while value != "":
        values.append(value)
        value = input("Enter a value: ")
    
    print("Here's the list:", values)

if __name__ == '__main__':
    main()
