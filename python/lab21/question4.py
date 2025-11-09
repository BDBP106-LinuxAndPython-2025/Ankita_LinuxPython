def checkList(lst, index):
    try:
        # Try to print the element at the given index
        print("Element at index", index, "is:", lst[index])
    except IndexError:
        print("Error: Index is out of range.")
    except TypeError:
        print("Error: Invalid input type. Please provide a list and an integer index.")

# (a) number list and valid index
checkList([10, 20, 30, 40], 2)

# (b) a string input and index
checkList("Hello", 1)

# (c) a boolean value (True) and index
checkList(True, 0)

# string input and incorrect index
checkList("Python", 10)
