def menu():
    print("1. Singly Linked List")
    print("2. Check if Palindrome")
    print("3. Priority Queue")
    print("4. Evaluate an Infix Expression")
    print("5. Graph")
    print("6. Exit")


def singlyLinkedListMenu():
    print("a. Add Node")
    print("b. Display Nodes")
    print("c. Search for & Delete Node")
    print("d. Return to main menu")


def priorityQueueMenu():
    print("a. Add a student")
    print("b. Interview a student")
    print("c. Return to main menu")


class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class singlyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, info):
        new_node = Node(info)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addNodeUserInput(self):
        user_input = int(input("Enter number: "))
        self.addNode(user_input)
        self.displayNodes()

    def displayNodes(self):
        current = self.head
        print("\nCurrent List: ", end="")
        while current != None:
            print(current.info, end=" ")
            current = current.next

        print("\n")

    def deleteNode(self, info):
        current = self.head
        if current.info == info:
            self.head = current.next
        else:
            while current:
                if current.info == info:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None
        self.displayNodes()


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, info):
        self.items.append(info)

    def pop(self):
        return self.items.pop()


def palindromeCheck():
    stack = Stack()
    reversed_text = ""

    user_input = input("Enter a string: ")

    for i in user_input:
        stack.push(i)

    while not stack.isEmpty():
        reversed_text = reversed_text + stack.pop()

    if user_input == reversed_text:
        print('The string is a palindrome.\n')
    else:
        print('The string is not a palindrome.\n')


class student:
    def __init__(self, name, midterm_grade, final_grade, personality):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.personality = personality

    def Comparison(self, other):
        if self.personality != other.personality:
            return self.personality
        elif self.final_grade > other.final_grade:
            return self.final_grade
        elif self.midterm_grade > other.midterm_grade:
            return self.midterm_grade


class priorityQueue:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def interview_student(self):
        self.students.sort(reverse=True)
        for i in self.students:
            print(f"Interviewing {i.name}")


def addStudent():
    name = input("Enter student's name: ")

    while True:
        try:
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            if 0 <= midterm_grade <= 100:
                break
            else:
                print("Enter a valid input between 0 and 100")
        except ValueError:
            print("Invalid input, enter a number.")

    while True:
        try:
            final_grade = int(input("Enter final grade (0-100): "))
            if 0 <= final_grade <= 100:
                break
            else:
                print("Enter a valid input between 0 and 100")
        except ValueError:
            print("Invalid input, enter a number.")

    personality = input("Does the student have a good personality? (yes/no): \n").lower()
    if personality == "yes":
        personality = True
    else:
        personality = False

    print(f"{name} midterm_grade: {midterm_grade}/100, final_grade: {final_grade}/100, good_attitude: {personality}")
    print()
    return student(name, midterm_grade, final_grade, personality)


def main():
    ll = singlyLinkedList()
    priority_queue = priorityQueue()

    node1 = Node(20)
    node2 = Node(10)
    node3 = Node(15)
    node4 = Node(7)

    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    while True:
        menu()
        choice = input("\nEnter choice 1 -> 6: ")

        if choice == "1":
            singlyLinkedListMenu()
            sub_choice = input("\nEnter choice a -> d: ").lower()
            if sub_choice == "a":
                ll.addNodeUserInput()
            elif sub_choice == "b":
                ll.displayNodes()
            elif sub_choice == "c":
                delete_value = int(input("Enter value to delete: "))
                ll.deleteNode(delete_value)
            elif sub_choice == "d":
                print("Exiting\n")
            else:
                print("Wrong input returning to menu.\n")
        elif choice == "2":
            palindromeCheck()
        elif choice == "3":
            priorityQueueMenu()
            sub_choice = input("\nEnter choice a -> c: ").lower()
            if sub_choice == "a":
                new_student = addStudent()
                priority_queue.add_student(new_student)
            elif sub_choice == "b":
                priority_queue.interview_student()


main()
