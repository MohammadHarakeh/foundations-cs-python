def menu():
    print("1. Add Matrices")
    print("2. Check Rotation")
    print("3. Invert Dictionary")
    print("4. Convert Matrix to Dictionary")
    print("5. Check Palindrome")
    print("6. Search for an Element & Merge Sort")
    print("7. Exit")

def addMatrices():
    print("hello")



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
