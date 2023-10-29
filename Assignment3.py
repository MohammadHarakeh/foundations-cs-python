def menu():
    print("1. Add Matrices")
    print("2. Check Rotation")
    print("3. Invert Dictionary")
    print("4. Convert Matrix to Dictionary")
    print("5. Check Palindrome")
    print("6. Search for an Element & Merge Sort")
    print("7. Exit")
    print()


def addMatrices():
    matrix1 = []
    matrix2 = []
    result = []

    row1 = int(input("enter the number of rows for matrix 1: "))
    column1 = int(input("enter the number of columns for matrix 1: "))
    print("")

    row2 = int(input("enter the number of rows for matrix 2: "))
    column2 = int(input("enter the number of columns for matrix 2: "))

    if row1 != row2 or column1 != column2:
        print("Matrices are not equal")
        addMatrices()

    for i in range(row1):
        print("input for row", i, "int the first matrix")
        matrix1.append([])
        for j in range(column1):
            print("input for column", j, "in the first matrix")
            print("")
            input1 = int(input("input into the first matrix: "))
            matrix1[i].append(input1)
    print("the first matrix is: ", matrix1)

    for i in range(row2):
        print("input for row", i, "in the second matrix")
        matrix2.append([])
        for j in range(column2):
            print("input for column", j, "in the second matrix")
            print("")
            input2 = int(input("input into the second matrix: "))
            matrix2[i].append(input2)
            print("the second matrix is: ", matrix2)

    for row1, row2 in zip(matrix1, matrix2):
        result_row = [x + y for x, y in zip(row1, row2)]
        # Zip is used to combine two or more lists
        result.append(result_row)
    print("The addition of the two matrices are: ")
    print()
    for row in result:
        print(row)


# addMatrice is O(N^2)

def checkRotation():
    matrix1 = []
    matrix2 = []

    row1 = int(input("enter the number of rows for matrix 1: "))
    column1 = int(input("enter the number of columns for matrix 1: "))
    print()

    row2 = int(input("enter the number of rows for matrix 2: "))
    column2 = int(input("enter the number of columns for matrix 2: "))

    if row1 != column2 or column1 != row2:
        print("They are not a rotation of each other")
        print()
        return menu()

    for i in range(row1):
        print("input for row", i, "int the first matrix")
        matrix1.append([])
        for j in range(column1):
            print("input for column", j, "in the first matrix")
            print("")
            input1 = int(input("input into the first matrix: "))
            matrix1[i].append(input1)
            print("the first matrix is: ", matrix1)

    for i in range(row2):
        print("input for row", i, "in the second matrix")
        matrix2.append([])
        for j in range(column2):
            print("input for column", j, "in the second matrix")
            print("")
            input2 = int(input("input into the second matrix: "))
            matrix2[i].append(input2)
            print("the second matrix is: ", matrix2)
            print("Matrix one: ", matrix1)
            print("Matrix Two: ", matrix2)

    for i in range(row1):
        for j in range(column2):
            if matrix1[i][j] != matrix2[j][i]:
                print("They are not a rotation of each other")
                print()
                return menu()
    else:
        print("They are a rotation of each other")


def invertedDictionary(input1):
    hashmap = {}
    for key, value in input1.items():
        if value in hashmap:
            hashmap[value].append(key)
        else:
            hashmap[value] = [key]
    return hashmap
# invertedDictionary is O(N)

def matrixDictionary():
    def matrixDictionary():
        input1 = int(input("Enter number of users: "))
        list1 = []
        hashmap = {}
        for i in range(input1):
            temp = []
            first_name = input("Enter first name: ")
            temp.append(first_name)

            last_name = input("Enter last name: ")
            temp.append(last_name)

            user_id = input("Enter your ID: ")
            temp.append(user_id)

            job_title = input("Enter your job title: ")
            temp.append(job_title)

            list1.append(temp)
        print(list1)


def main():
    while True:
        name = str(input("What is your name? "))
        print(f"Hello {name} what would you like to do? ")
        print("")

        menu()
        choice = input("Enter your choice from 1 -> 7: ")
        print("")

        if choice == '1':
            addMatrices()
        elif choice == '2':
            checkRotation()
        elif choice == '3':
            hashmap = {}
            num_items = int(input("Enter the number of items in the dictionary: "))

            for i in range(num_items):
                key = input("Enter a key: ")
                value = input("Enter a value: ")
                hashmap[key] = value

            print("Before inverting:", hashmap)

            inverted_hashmap = invertedDictionary(hashmap)

            print("After inverting:", inverted_hashmap)

        elif choice == '4':
            matrixDictionary()


main()
