numbers = []
even_numbers = []

while True:
    user_input = input("Enter an integer or type 'QUIT' to stop: ")
    if user_input == "QUIT":
        break
    else:
        num = int(user_input)
        numbers.append(num)
        if num % 2 == 0:
            even_numbers.append(num)

print("The list of numbers: ", numbers)
print("The list of even numbers: ", even_numbers)
