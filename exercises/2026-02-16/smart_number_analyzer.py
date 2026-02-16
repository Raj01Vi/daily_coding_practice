print("Enter a number")
number = int(input(">"))


if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


if number > 0:
    for i in range(1, number + 1):
        print(i, end=" ")
elif number < 0:
    print(abs(number))

print()