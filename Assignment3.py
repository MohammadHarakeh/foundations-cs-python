import sys


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

    row1 = int(input("enter the number of rows for matrix 1: "))
    column1 = int(input("enter the number of columns for matrix 1: "))
    print("")

    row2 = int(input("enter the number of rows for matrix 2: "))
    column2 = int(input("enter the number of columns for matrix 2: "))

    if row1 != row2 or column1 != column2:
        print("Matrices are not equal")
        addMatrices()

    for i in range(row1):
        print("input for row", i)
        matrix1.append([])
        for j in range(column1):
            print("input for column", j)
            print("")
            input1 = int(input("input into the first matrix: "))
            matrix1[i].append(input1)
    print("the first matrix is: ", matrix1)

    for i in range(row2):
        print("input for row", i)
        matrix2.append([])
        for j in range(column2):
            print("input for column", j)
            print("")
            input2 = int(input("input into the second matrix: "))
            matrix2[i].append(input2)
            print("the second matrix is: ", matrix2)

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result = [matrix1[i][j] + matrix2[i][j]]
    print(result)




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


main()

