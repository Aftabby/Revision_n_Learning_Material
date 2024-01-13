#Inserting element in the list 
item =[1,3,4,5,6]
print(item)
item.insert(1, 2)   #To insert use --- list_name.insert(index_number, value) -- it will not delete any element, it will just slid in that element in that index
print(item)



#Remove duplicate chars from the string
def remove_duplicate(str1):
    new_str = ""
    for char in str1:
        if char not in new_str:
            new_str += char
    return new_str

string_one = "Hello world! HOw are all of you??"
string_one = remove_duplicate(string_one)
print(string_one)






#Find the second smallest of a list
def second_smallest(nums):
    nums.sort() # Or you can use--- nums = sorted(nums) -- does the same thing
    return nums[1]

nums = [ 5, 75, 89, 12, 44, 23, 22]
print(second_smallest(nums))
#----Another approach -----
nums.remove(min(nums))
print(min(nums))







#Find the second largest of a list
def second_largest(nums): # variable inside a function is different from the variable outside or global variable
    sec_large = max(nums)
    nums.remove(sec_large)
    sec_large = max(nums)
    return sec_large

nums = [ 5, 75, 89, 12, 44, 23, 22]
sec_large = second_largest(nums)
print(sec_large)
#---------Another approach------------
nums = [ 5, 75, 89, 12, 44, 23, 22]
nums.sort()
print(nums[-2])  # Reverse Index: when you -1 as index it will point to the last element of the list, same way -2 will point to the second last element of the list
# ---------------- Another approach--------------
nums.sort(reverse = True) 
print(nums[1]) # Using listName.sort(reverse = True) will sort the list in descending order








#Sum of Squares
num = int(input("Enter a number:\n"))
sum_up = 0
for i in range(num+1):
    print("value of i", i, "\n")
    sum_up += i**2
print(sum_up)
#--------Another approach
def sum_of_square(num):
    num = num*(num+1)*(2*num+1)/6 # When you divide and assign variable, the data type of that variable become float type 
    return num
print(sum_of_square(num))









#Find the largest element of a list
nums = [ 5, 75, 89, 12, 44, 23, 22]
highest_num = max(nums)
print(highest_num)
#--------Another Approach
highest_num = nums[0]
for i in nums:
    if i > highest_num:
        highest_num = i
print(highest_num)









# Easy way sum up a list
nums = [ 5, 75, 89, 12, 44, 23, 22]
sum_of_nums = sum(nums)
print(sum_of_nums)





#Important Notes
# Use the sum function to add element of a list
# Use max function to get the highest number out of a list && Use min for smallest
# Reverse Index: when you -1 as index it will point to the last element of the list, same way -2 will point to the second last element of the list
# Using listName.sort(reverse = True) will sort the list in descending order
# 'not in' KW is just the opposite of 'in' KW
# To insert any element in the list use --- list_name.insert(index_number, value) -- It will just slide in that index number, pushing the rest elements backward