first_list = []
for i in range(5):
    num = int(input(f"Enter integer number {i+1} for the first list: "))
    first_list.append(num)

second_list = []
for i in range(5):
    num = int(input(f"Enter integer number {i+1} for the second list: "))
    second_list.append(num)

common_list = list(set(first_list) & set(second_list))

print("The first list:", first_list)
print("The second list:", second_list)
print("The common list:", common_list)
