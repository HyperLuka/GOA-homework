for i in range(21):
   print(i)
 

for i in range(1, 11):
    print(i)

for i in range(0, 101, 2):
    print(i)


number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


age = int(input("Enter your age: "))
if age > 18:
    print("you are adult")
else:
    print("you are virgin")


day_number = int(input("Enter a number (1-7): "))
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
 print("Invalid number! Please enter a number between 1 and 7")