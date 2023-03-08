import random
r = random.randint(1, 100)
print(r)
while True:
    num = input("Guess a number:")
    num = int(num)
    if r == num:
        print("You got it!")
        break
    elif r > num:
        print("Smaller than answer")
    else:
        print("Bigger than answer")