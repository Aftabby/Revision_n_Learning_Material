#To iterate over each element of a series of elements(list, set etc.) run -- for loop -- 
#To run a loop based on condition run while loop, (must provide a break condition)

#  ====     For LOOP   =======
basket = ["Apple", "Orange", "Strawberry", "Banana"]
#In below for loop -- fruit -- is a loop variable - the value of this variable will be each element in the list,, in every iteration the value will be changing from the first element of the list to the last element -- 
# 'in' is a keyword just to check if the statement is true that the loop variable value contains among the list elements --
# the last word before colon is the name of the list variable on which you want to run the for loop -- 
# the colon and the indentation is mandatory in python
# For every iteration the a particular element will be assigned to the loop variable sequentially, respectively with index number, and the tasks under loop (indented code) will perform its action
for fruit in basket:
    print("Fresh " + fruit)


# New Example of for loops
numList = [ 15, 54, -34, 22, 66, 106, 19, 67, 143]

for num in numList:
    if num > 55:
        break
    if num % 2 == 0:
        continue
    print(num)


# =======  While LOOPS   ==============
print("While loop Started")

# Declare a loop variable 
# -- Write the while KW 
# -- Add a stopping condition after the while 
# -- Underneath while, write the repeating work 
# -- Update the loop variable
count = 0
while count < 5:
    print(count)
    count = count + 1


#while loop examples & practices
count = 0
sum = 0
while count <= 10:
    sum = sum + count
    count = count + 1

print(sum)

sum = 0
count = 0
while count < 50:
    if count % 2 == 0:
        count = count + 1 
        continue
    sum = count + sum
    count += 1 #count += 1 is count = count + 1
print(sum)