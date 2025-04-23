def main():
    curr_value = int(input("Enter a number: "))  # Get initial number from user

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
