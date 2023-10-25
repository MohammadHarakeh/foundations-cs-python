# # Question 1:
def reverse(s, i):
    return s[::-1] * i

s = str(input("Enter the String: "))
i = int(input("Enter the amount to repeat: "))
print(reverse(s,i))

# Question 2:
def upperLower(z):
    x = ""
    y = ""
    for i in range(len(z)):
        if z[i].isupper():
            x = x + z[i]
        elif z[i].islower():
            y = y + z[i]
    return x + y


s = input("Enter word: ")
print(upperLower(s))

# Question 3:
def anagram(s1, s2):
    hashmap1, hashmap2 = {}, {}

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        hashmap1[s1[i]] = 1 + hashmap1.get(s1[i], 0)
        hashmap2[s2[i]] = 1 + hashmap2.get(s2[i], 0)
    if hashmap1 == hashmap2:
        return True
    return False


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(anagram(s1, s2))

# Question 4
def maxNum(l):
    max_number = l[0]
    max_index = 0

    for i in range(1, len(l)):
        if l[i] > max_number:
            max_number = l[i]
            max_index = i

    return max_number, max_index


l = [5, 6, 3, 2, 7, 2, 0, 1, 6]
max_value, max_index = maxNum(l)
print(f"Max number is {max_value} at index {max_index}")

def minNum(l):
    min_number = l[0]
    min_index = 0

    for i in range(1, len(l)):
        if l[i] < min_number:
            min_number = l[i]
            min_index = i

    return min_number, min_index

l = [5, 6, 3, 2, 7, 2, 0, 1, 6]
min_value, min_index = minNum(l)
print(f"Min number is {min_value} at index {min_index}")


# question 5
def digitSum(n):
    if n == 0:
        return 0
    last_digit = n % 10
    remaining = n // 10
    return last_digit + digitSum(remaining)


number = 1234
print(digitSum(number))

# question 6
def removeDuplicates(s):
    if len(s) <= 1:
        return s

    if s[0] == s[1]:
        return removeDuplicates(s[1:])
    else:
        return s[0] + removeDuplicates(s[1:])

str1 = input("Enter a string: ")
print(removeDuplicates(str1))

# question 7
def reverseNumbers(n):
    if n == 0:
        return ""
    last_digit = n % 10
    remaining = n // 10
    return str(last_digit) + reverseNumbers(remaining)


n = int(input("Enter numbers to reverse them: "))
print(reverseNumbers(n))
