
for i in range(21):
   print()


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
print()



for i in range(0, 21, 2):
    print(i)
print()



sum = 0
for i in range(50, 101):
    sum += i
print("Sum:", sum)
print()


for i in range(1, 51):
    if i % 5 == 0:
        print(i)
print()


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
smaller = min(num1, num2)
larger = max(num1, num2)
for i in range(smaller, larger + 1):
    print(i)
print()



product = 1
for i in range(5, 11):
    product *= i
print("Product:", product)
print()



word = "PYTHON"
for char in word:
    print(char)

