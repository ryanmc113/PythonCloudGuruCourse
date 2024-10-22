namesAndAges = {'ry': 31, 'heather':44, 'harry':35}

for key,value in namesAndAges.items():
    print(key,value)
   
for name,age in namesAndAges.items():
    print(f"Person name: {name}" )
    print(f"Age of the person: {age}")



count = 1
for _ in range(4):
    print("looping")

colors = ['red', 'blue', 'orange', 'green', 'yellow']
# uppercase_colors = []
# for color in colors:
#     uppercase_colors.append(color.upper())

uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]

print(warm_colors)


upper_num = int(input("How many values should we process: "))

for num in range(1,upper_num +1):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)

count = 0
while(count < 5):
    print("too low")
    count += 1
