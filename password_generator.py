import random

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

lenght = int(input("Random password lenght do you want:"))
random_random = alphabets
random_random += str(numbers)
random_random += symbols
pass_random = []  #gather all random to list

for randm in range(lenght):  #pick all random character
  pass_random += random.choice(random_random)

random.shuffle(pass_random)  #shuffle all the random list
final_random_pass = ""

for result in pass_random:
  final_random_pass += result
remove_space = "".join(
    final_random_pass.split())  #to remove space in randomization
if lenght < 8:
  print("Weak Password")
elif lenght <= 12:
  print("Strong Password")
elif lenght <= 26:
  print("Very Strong Password")
else:
  print("Very Very Strong Password!!!")
print(remove_space)