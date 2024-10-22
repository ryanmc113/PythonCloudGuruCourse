nameInput = input("put any name: ")

def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    
    dictionaryName = {'first_name':first_name, 'last_name':last_name}
    print(dictionaryName)

split_name(nameInput)

itemInput = input("put a word in, any word and watch the magic: ")
def is_palindrome(item):
    item = str(item)
    return item == item[::-1]
print(is_palindrome(itemInput))

wordInput = input("what word would like repeated? ")
numInput = int(input("How many times would you like the word to be repeated? "))

def built_list(word, num):
    final_list = []
    for _ in range(num):
        final_list.append(word)
    print(final_list)

built_list(wordInput, numInput)