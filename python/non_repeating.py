# return the first non repeating character in a string

# create an empty dictionary where you can store each character of the string
# store it as a key:value
# NEXT: iterate through string and start count 
# NEXT if the value is 1, print it 
# create an else: return False

def non_repeating(string):

    #setting empty dicts
    counting = {}


# start iterating through the string and if the element is not in the dict, add it and add a 1
# if item is already in dict, add 1 to the value 
    for i in string:
        counting[i] = counting.get(i,0) + 1
        
    # if element in string is  == 1, print it 
    for x in string:
        if counting[x] == 1:
            print (x)

    return False
non_repeating("abcdabcde")
