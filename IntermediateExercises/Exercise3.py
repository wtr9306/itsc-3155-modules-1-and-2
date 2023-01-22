def count_letters(string):
    letter_count = {}
    for letter in string.lower():
        if letter != " ":
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

user_string = input("Enter a string: ")
letter_count = count_letters(user_string)
print("Letter count:", letter_count)
