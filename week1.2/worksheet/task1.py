# Worksheet 1.2: Task 1 Solution
import sys

try:
    print("Hello")
    num = int(input("Enter a number between 0 and 100: "))

except: 
        
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit()

if num <= 100 and num >= 0:
    if num >= 70:
        result = "Distinction"

    elif num >= 40:
        result = "Pass"

    else:
        result = "Fail"

else:
    sys.exit("Error: Grade must be an integer between 0 and 100")

print(f'{num} is a {result}')