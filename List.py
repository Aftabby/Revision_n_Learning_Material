      # # # # ALL ABOUT LIST # # #

#Two lists, one of number and another of strings
myFirstList = [ 16, 20, 45, 67, 33, 45, 252]            #You can also add various types of data-types in a singular list (str, int, float etc.)
mySecondList = [ "one", "two" , "three", "four", "fourty Nine"]

#Adding a value at the last of the list     -- list_name.append(new_value) --
myFirstList.append(5)
mySecondList.append("five")

#printing a list with all elements inside it 
print(myFirstList)
print(mySecondList)

#removing a value from the value, for two or more same value, it will remove only the first one , -- list_name.remove(value)
myFirstList.remove(45)

# Getting the index number of a list element  -- list_name.index(value)
index_count = mySecondList.index("three")   

# To replace any element of list by index number
mySecondList[3] = "six"

#printing a list with all elements inside it 
print("After appending, inserting and removing:")
print(myFirstList)
print(mySecondList)

# To find the value by index number of a list - listName[startIndex : endIndex : step] -- starting from the start index(including) up to the end_index(excluding) and by default the step is 1, 
i1 = mySecondList[2]
i2 = mySecondList[2:]
i3 = mySecondList[1:3]
i4 = mySecondList[:3]
i5 = mySecondList[::2]

print(f"i1: {i1}\ni2: {i2}\ni3: {i3}\ni4:  {i4}\ni5: {i5}")

#to find out the total number of elements in a list, (last index number + 1)
numOfElements = len(mySecondList)


#the minimum value from a list
minValue1 = min(mySecondList)
minValue0 = min(myFirstList)

#the maximum value from a list
maxValue1 = max(mySecondList)
maxValue0 = max(myFirstList)

#TO check if an element exists in the list or not, output in boolean type variable
doesExist = "three" in mySecondList
doesExist0 = 53 in myFirstList

#Adding two lists together, the new lists will be the combination of all the elements respectively
addedList = myFirstList + mySecondList + myFirstList

#Remove the item of the list by index number
mySecondList.pop() #By default it will remove the last element of the list
mySecondList.pop(2)  # To remove an element by index number, pass the index number as an argument of pop function

#Sorting a list, within that list - organize the elements of a list in ascending order
myFirstList.sort()
mySecondList.sort()

#Reversing all elements order of a lists - first element in last and last one in first
myFirstList.reverse()
mySecondList.reverse()

#Finding out a range of Numbers - range(start, stop) - by default start is 0, and uptp stop (excluding stop)
anotherTemp = range(8)
anotherTemp1 = range( 9, 17)



#queries  and Important Notes
#how to determine which string is greater than one another?
#What the range(start, stop) function return?
# YOU  CAN PUT NUMBER & STRING TYPE VALUE IN THE SAME LIST, BUT THEN YOU CAN'T COMPARE THEM FOR MIN OR MAX
