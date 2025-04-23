MAX_LENGTH = 3

def shorten(lst):
    """
    Removes elements from the end of lst and prints each one removed,
    until the list is MAX_LENGTH items long.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()

