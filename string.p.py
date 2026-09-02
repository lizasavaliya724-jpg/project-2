# # 1. Convert string into uppercase
# text = input("Enter a string: ")
# print("Uppercase:", text.upper())

# 2. Convert string into lowercase
# text = input("Enter a string: ")
# print("Lowercase:", text.lower())

# 3. Remove all spaces from a string
# text = input("Enter a string: ")
# print("Without spaces:", text.replace(" ", ""))

# 4. Count the number of characters in a string
# text = input("Enter a string: ")
# print("Number of characters:", len(text))


# 5. Reverse a string
# text = input("Enter a string: ")
# print("Reversed string:", text[::-1])

# # 6. Check whether a string is a palindrome
# text = input("Enter a string: ")
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")/

# 7. Count vowels and consonants in a string
# text = input("Enter a string: ").lower()
# vowels = "aeiou"
# v_count = sum(1 for ch in text if ch in vowels)
# c_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
# print("Vowels:", v_count)
# print("Consonants:", c_count)

# 8. Replace all spaces with underscores
# text = input("Enter a string: ")
# print("With underscores:", text.replace(" ", "_"))

# 9. Remove all non-alphabetical characters
# import re
# text = input("Enter a string: ")
# only_letters = re.sub("[^a-zA-Z]", "", text)
# print("Only alphabets:", only_letters)

# 10. Extract and print only digits from a string
text = input("Enter a string: ")
digits = "".join(ch for ch in text if ch.isdigit())
print("Digits:", digits)
