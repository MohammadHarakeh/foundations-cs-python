def menu():
    print("1. Add Matrices")
    print("2. Check Rotation")
    print("3. Invert Dictionary")
    print("4. Convert Matrix to Dictionary")
    print("5. Check Palindrome")
    print("6. Search for an Element & Merge Sort")
    print("7. Exit")

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
        result_row = [x + y for x, y in zip(row1,row2)]
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

    if column1 == row2 and row1 == column2:
        print("Matrix 1 and Matrix 2 have compatible dimensions for rotation.")
        for row in matrix2:
            for element1 in row:
                print(element1, end=' ')
            print()
        for row in matrix1:
            for element2 in row:
                print(element2, end=' ')
                print()
    else:
        print("Matrix 1 and Matrix 2 do not have compatible dimensions for rotation.")



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


main()

