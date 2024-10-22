message = input("enter now!!!: ")
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())

words = message.lower().split()
print(words)

sort_words = sorted(words)
print(sort_words)