numbers = []

for _ in range(5):
    number = int(input("Enter a Number: "))
    numbers.append(number)

print("List is: ", numbers)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest: ", largest)

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest: ", smallest)

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print(f"Average: {average:.2f}")

even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1

print("Count of even numbers: ", even_count)