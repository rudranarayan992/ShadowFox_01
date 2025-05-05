# Task 3: Demonstration of 'for' loop usage in Python

# 1. Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=' ')
print("\n---")

# 2. Print even numbers between 1 and 20
print("Even numbers between 1 and 20:")
for i in range(2, 21, 2):
    print(i, end=' ')
print("\n---")

# 3. Loop through a string
text = "ShadowFox"
print(f"Characters in '{text}':")
for char in text:
    print(char)
print("---")

# 4. Loop through a list and print each element
fruits = ["apple", "banana", "cherry", "date"]
print("Fruit list:")
for fruit in fruits:
    print(fruit)
print("---")

# 5. Nested for loop: Multiplication table (1 to 5)
print("Multiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("------")
