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


def graphMenu():
    print("a. Add vertex")
    print("b. Add edge")
    print("c. Remove vertex")
    print("d. Remove edge")
    print("e. Display vertices with a degree of X or more.")
    print("f. Return to main menu")


class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class singlyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # This is of O(N) time complexity because of the while loop
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

    # This is of O(N) time complexity because of the while loop
    def addNodeUserInput(self):
        while True:
            user_input = input("Enter number: ")
            print()
            if user_input.isdigit():
                self.addNode(user_input)
                break
            else:
                print("Wrong input")

    # This is of O(N) time complexity because of the while loop
    def displayNodes(self):
        current = self.head
        print("\nCurrent List: ", end="")
        while current != None:
            print(current.info, end=" ")
            current = current.next
        print("\n")

    # This is of O(N) time complexity because of the while loop
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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # This is of O(1) because we are only appending from the list
    def push(self, info):
        self.items.append(info)

    # This is of O(1) since we are only popping from the list
    def pop(self):
        return self.items.pop()

    # This is of O(1) time complexity
    def peek(self):
        return self.items[len(self.items) - 1]

    # This is of O(1)
    def size(self):
        return len(self.items)


# This is of O(N) time complexity since it is the amount of time that it will take to push to the user_input and popping from the stack
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


# This is O(1) time complexity
def compute(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2


# The entire function is O(N) since it will depend on the size of the expression
def infix(equation):
    prec_dictionary = {"(": 0, ")": 0, "*": 2, "/": 2, "+": 1, "-": 1}
    operator_stack = Stack()
    operand_stack = Stack()
    allowed_operators = "+-/*"

    i = 0
    while i < len(equation):
        char = equation[i]

        if char in allowed_operators:
            while not operator_stack.isEmpty() and prec_dictionary[char] <= prec_dictionary[operator_stack.peek()]:
                value2 = operand_stack.pop()
                operator = operator_stack.pop()
                value1 = operand_stack.pop()
                result = compute(value1, value2, operator)
                operand_stack.push(result)
            operator_stack.push(char)
            i += 1
        elif char == "(":
            operator_stack.push(char)
            i += 1
        elif char == ")":
            while operator_stack.peek() != "(":
                value2 = operand_stack.pop()
                operator = operator_stack.pop()
                value1 = operand_stack.pop()
                result = compute(value1, value2, operator)
                operand_stack.push(result)
            operator_stack.pop()
            i += 1
        else:
            j = i
            while j < len(equation) and (equation[j].isdigit() or equation[j] == '.'):
                j += 1
            operand = equation[i:j]
            operand_stack.push(float(operand))
            i = j

    while not operator_stack.isEmpty():
        value2 = operand_stack.pop()
        operator = operator_stack.pop()
        value1 = operand_stack.pop()
        result = int(compute(value1, value2, operator))
        operand_stack.push(result)

    return operand_stack.pop()


# This is O(N) since it depends on the above function
def infixUserInput():
    user_input = str(input("Enter an infix expression without spaces: "))
    return infix(user_input)


class student:
    def __init__(self, name, midterm_grade, final_grade, personality):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.personality = personality

    # This is O(1) Time complexity
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

    # This is O(1) time complexity
    def add_student(self, student):
        self.students.append(student)

    # This is O(N) time complexity since we are sorting
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


class Graph:
    def __init__(self):
        self.vertices = {}

    # This is O(1)
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        print("Added Vertex\n")

    # This is O(1) time complexity
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        print("Added Edges\n")

    # This is O(1) time complexity
    def removeVertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.pop(vertex)
        print("Removed Vertex\n")

    # This is O(N) time compexity
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
            if vertex1 in self.vertices[vertex2]:
                self.vertices[vertex2].remove(vertex1)
            print("Removed Edges\n")
        else:
            print("Vertices not found\n")

    # This will be O(N) depending on the number of graphs to display
    def display(self):
        display_input = int(input("Enter degree to display: "))
        print("This is the entire graph")
        for i, j in self.vertices.items():
            print(f"{i} : {j}")
        print()
        print(f"These are of degree {display_input}: ")
        for i, j in self.vertices.items():
            if len(j) >= display_input:
                print(f"{i}: {len(j)}")
        print()


def main():
    ll = singlyLinkedList()
    priority_queue = priorityQueue()
    graph = Graph()
    counter = 0

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
        sub_choice = ""
        if counter == 3:
            break

        if choice == "1":
            while sub_choice != "d":
                singlyLinkedListMenu()
                sub_choice = input("\nEnter choice a -> d: ").lower()
                if sub_choice == "a":
                    ll.addNodeUserInput()
                    counter = 0
                elif sub_choice == "b":
                    ll.displayNodes()
                    counter = 0
                elif sub_choice == "c":
                    delete_value = int(input("Enter value to delete: "))
                    ll.deleteNode(delete_value)
                    counter = 0
                elif sub_choice == "d":
                    print("Exiting\n")
                    counter = 0
                else:
                    counter += 1
                    print(f"Wrong input you have {4 - counter} tries left.\n")
            counter = 0

        elif choice == "2":
            palindromeCheck()
            counter = 0

        elif choice == "3":
            counter = 0
            while sub_choice != "c":
                priorityQueueMenu()
                sub_choice = input("\nEnter choice a -> c: ").lower()
                counter = 0
                if sub_choice == "a":
                    new_student = addStudent()
                    priority_queue.add_student(new_student)
                    counter = 0
                elif sub_choice == "b":
                    priority_queue.interview_student()
                    counter = 0
                elif sub_choice == "c":
                    print("Exiting\n")
                    counter = 0
                else:
                    counter += 1
                    print(f"Wrong input you have {4 - counter} tries left.\n")

        elif choice == "4":
            result = infixUserInput()
            print(result, "\n")
            counter = 0

        elif choice == "5":
            counter = 0
            while sub_choice != "f":
                graphMenu()
                print()
                sub_choice = input("\nEnter choice a -> f: ").lower()
                if sub_choice == "a":
                    add_vertex = input("Enter a vertex to add: ").upper()
                    graph.addVertex(add_vertex)
                    counter = 0
                elif sub_choice == "b":
                    edge1 = input("Enter first vertex: ").upper()
                    edge2 = input("Enter second vertex: ").upper()
                    graph.addEdge(edge1, edge2)
                    counter = 0
                elif sub_choice == "c":
                    remove_vertex = input("Enter a vertex to remove: ").upper()
                    graph.removeVertex(remove_vertex)
                    counter = 0
                elif sub_choice == "d":
                    edge1 = input("Enter first vertex: ").upper()
                    edge2 = input("Enter second vertex: ").upper()
                    graph.removeEdge(edge1, edge2)
                    counter = 0
                elif sub_choice == "e":
                    graph.display()
                    counter = 0
                elif sub_choice == "f":
                    print("Exiting\n")
                    counter = 0
                else:
                    counter += 1
                    print(f"Wrong input you have {4 - counter} tries left.\n")

        elif choice == "6":
            print("Exiting Program")
            break

        else:
            counter += 1
            print(f"Wrong input you have {4 - counter} tries left.\n")


main()
