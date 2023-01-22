sum = 0

for i in range(5):
    while True:
        try:
            num = int(input(f"Enter integer number {i+1}: "))
            sum += num
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("The sum of the integers is: ", sum)
