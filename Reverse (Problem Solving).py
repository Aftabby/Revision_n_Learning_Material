#Reverse the words only
def rev_wordss(str2):
    str2 = str2.split()     # If you don't pass any parameter, split method will split the words by whitespaces and return a list of all the individual words, if you pass a character as a parameter it will break the string by that character.
    str2.reverse()          # .reverse() method reverses a list
    rev_str = ' '.join(str2)  # The opposite of split is join method, it adds all the the element/string of a list/array together, if you want to join them by whitespaces run ---  ' '.join(array)
    
    print(rev_str)

str2 = "Hello huney bunny dongor fongor"

rev_wordss(str2)










#Reverse Domain
sites = "www.programming-hub.com"
parts = sites.split('.')    #Returns a split list
parts.reverse()
parts = '.'.join(parts)     # -- ''.join(list_name) -- is a string class method, which adds every element of list, and adds the string on which it was called upon (here it is -- dot(.)) , between all the elements
print(parts)
#----------ANother approach--------
site = "www.programming-hub.com"
rev = '.'.join(reversed(site.split('.')))       # list_name.reverse() -- and -- reversed(list_name) does the same thing
print(rev)