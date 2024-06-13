#დავალება:შექმენით WHILE ციკლი და დაბეჭდეთ 10ჯერ თქვენი სახელი while ციკლის გამოყენებით
count = 0
while count < 10:
    print("Luka")
    count += 1

#დავალება შექმენით გამოცნობის ტამაში

# Guess Game

num = 0

while num != 5:
    num = int(input("please enter number: "))

    if num == 5:
        print("You won!")
    else:
        print("You lose, try again!")