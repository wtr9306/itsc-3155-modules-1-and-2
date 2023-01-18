original_list = []
unique_list = []

for i in range(10):
    num = int(input(f"Enter integer number {i+1}: "))
    original_list.append(num)

for num in original_list:
    if original_list.count(num) == 1:
        unique_list.append(num)

print("Original List: ", original_list)
print("List with unique elements: ", unique_list)
