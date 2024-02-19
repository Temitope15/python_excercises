#program that prints all the factors of a number
num = 24
for i in range(1 , num+1):
    if num % i == 0:
        print(i, "is a factor of", num)