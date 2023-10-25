# Question 1
# a) 915
# b) 897
# c) 897
# d) 915
# e) 1
# f) 2.5
# g) 2
# h) 2.5
# i) 2.5
# j) 0

question1 = 10*(90+2)-5
question2 = 10*90+2-5
question3 = 10*90+(2-5)
question4 = 10.0*(90+2)-5
question5 = 120/(20+40)-(6-2)/4
question6 = 5.0/2
question7 = 5/2
question8 = 5.0/2.0
question9 = 5/2.0
question10 = 678%3*(8-(9/4))

print("Question 1: ", question1)
print("Question 2: ", question2)
print("Question 3: ", question3)
print("Question 4: ", question4)
print("Question 5: ", question5)
print("Question 6: ", question6)
print("Question 7: ", question7)
print("Question 8: ", question8)
print("Question 9: ", question9)
print("Question 10: ", question10)

# Question 2

input_id = input("Enter your ID: ")
id = "0" + input_id

name = input("Enter your name: ").upper()

dob = input("Enter the date of birth using DD/MM/YYYY: ").replace("-", "/")

address = input("Enter your address: ").strip().lower()

print("Your profile - ID: "+id, "name: "+name, "DOB: "+dob, "Address: "+address)

# Question 3

number = input()
if number.isdigit():
    print(number, "has", len(number), "digits")
else:
    print("Not a number")


# Question 4

numeric_grade = int(input())

if numeric_grade < 60:
    print(f"{numeric_grade} is equivalent to a F")

elif 60 <= numeric_grade < 63:
    print(f"{numeric_grade} is equivalent to a D-")

elif 63 <= numeric_grade < 67:
    print(f"{numeric_grade} is equivalent to a D")

elif 67 <= numeric_grade < 70:
    print(f"{numeric_grade} is equivalent to a D+")

elif 70 <= numeric_grade < 73:
    print(f"{numeric_grade} is equivalent to a C-")

elif 73 <= numeric_grade < 77:
    print(f"{numeric_grade} is equivalent to a C")

elif 77 <= numeric_grade < 80:
    print(f"{numeric_grade} is equivalent to a C+")

elif 80 <= numeric_grade < 83:
    print(f"{numeric_grade} is equivalent to a B-")

elif 83 <= numeric_grade < 87:
    print(f"{numeric_grade} is equivalent to a B")

elif 87 <= numeric_grade < 90:
    print(f"{numeric_grade} is equivalent to a B+")

elif 90 <= numeric_grade < 93:
    print(f"{numeric_grade} is equivalent to a A-")

elif 93 <= numeric_grade < 97:
    print(f"{numeric_grade} is equivalent to a A")

elif numeric_grade >= 97:
    print(f"{numeric_grade} is equivalent to a A+")


# Question 5

user_input = int(input("Enter a number to print a Pattern: "))

for i in range(0, user_input):
    for j in range(0, i+1):
        print("*", end="")
    print()

for i in range(1, user_input + 1):
    for j in range(user_input - i):
        print("*", end="")
    print()



# question 6:

input1 = int(input("Enter the first input: "))
input2 = int(input("Enter the second input: "))
if input1 > input2:
    print("Second input shouldn't be smaller than the first")
elif input1 == input2 and input2 % 2 != 0:
    print("No even numbers")
else:
    for i in range(input1, input2 + 1):
        if i % 2 == 0:
            print(i)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))


def power(num, numpow):
    if numpow == 0:
        return 1
    else:
        return num * power(num, numpow - 1)

print(power(2,3))