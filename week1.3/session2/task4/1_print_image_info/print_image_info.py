# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

with open("week1.3/session2/task4/images/feep.pgm" ,"r") as file:
    for i in range(3):
        if i == 1: 
            file.readline()
        elif i == 2:
            data = file.readline()
            #data = data.split(",")
            
            print(data)
            x = data[0]
            #y = data[1]
            print(f"resolution is {x} x ")

        


# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)