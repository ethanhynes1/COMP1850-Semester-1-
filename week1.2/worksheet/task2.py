# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys 

try:
    a = read_numbers()
    a.sort()
    length = len(a)
    mid = length // 2
    sum = sum(a)



    if length % 2 == 1:
        
        median = a[((length+1)//2)-1] 

    else:   

        median = (a[(length//2)-1] + a[(length//2)])/2

#print(median)
    

    min = min(a)
    max = max(a)
    #med = a[median]
    mean = sum/length
    print(f"Minimum = {min}")
    print(f"Maximum = {max}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")

    


except:
    
    sys.exit("Error: no numbers provided")

