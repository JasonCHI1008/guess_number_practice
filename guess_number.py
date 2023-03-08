import random
start = input("Please decide the random number range start value:")
end = input("Please decide the random number range end value:")
start = int(start)
end = int(end)
r = random.randint(start, end)
print(r)
count = 0
while True:
    num = input("Guess a number:")
    num = int(num)
    count += 1 #count = count + 1
    if r == num:
        print("You got it!")
        print("This is your", count, "try.")
        break
    elif r > num:
        print("Smaller than answer")
    else:
        print("Bigger than answer")
    print("This is your", count, "try.")