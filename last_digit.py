# a program that can get last digit, last two digits and last n digits based on the user input
power = 20
num = 2 ** power
last_digit = num % 10
print("The last digit is:", last_digit)
# last two digits
last_two_digits = num % 100
print("The last two digits are:", last_two_digits)
num_last_digits = 3
last_n_digits = num % (10 ** num_last_digits)
print("the last", num_last_digits, "digits are:", last_n_digits)