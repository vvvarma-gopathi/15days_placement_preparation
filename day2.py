#Day 2 Assignment 
#Task - A

print('='*25,'remove duplicates from list','='*25)

def remove_duplicates(lst):
    seen=set()
    result=[]
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result

print(remove_duplicates([1,2,2,1,3,4,5,6,7,6,7]))
print(remove_duplicates(['telugu','english','hindi','english','marati','hindi']))
print(remove_duplicates([21,22,23,21,23,24,24,25]))
print(remove_duplicates([1,2,1,2,3,2,1,4,5,6,5,7]))

print('='*25,' maximum sum of any contiguous window of size k','='*25)

def maximum_sum(lst,k):
    if k<=0:
        return -1
    max_sum=-9999999
    for i in range(len(lst)-k):
        if sum(lst[i:i+k])>max_sum:
            max_sum=sum(lst[i:i+k])
    return max_sum

print(maximum_sum([1, 2, 3],0))
print(maximum_sum([2, 1, 5, 1, 3, 2],3))
print(maximum_sum([4, 2, 1, 7, 5],1))
print(maximum_sum([-2, -3, -1, -5],2))

#Task - C 

print('='*25,' Debugging: Correct the Not found loop so it prints exactly one result. Explain why the original output was incorrect.','='*25)

def find_element(lst,target):
    for i in lst:
        if i == target:
            return 'Found'
    else:
        return "Not Found"

print(find_element([1,2,3,4,5,65,67,34,2,5],25))
print(find_element([21,23,14,56,78,89],89))
print(find_element([23,12,24,56,76,89,20],12))
#here in this case the else block which is written after for loop can only be executed
#after the execution of total for loop iterations so we only get Not found once in case 
#of the element is absent in the list



#Task - D

print('='*25,' maximum sum of any contiguous window of size k','='*25)

#LIST
#list is a mutable datatype it can will store the elements cosecutively it is like a 
#dymically typed array in python
#it is used when the data has to under goes into manipultion
#by using list we can validate the multiple schemas of responses in backend
#while defining the cors at backend we use list to mention multiple frontend origins

#DICT 
#dict is a key value paired data collection which is a mutable data structure in python
#dict can also be used as a hashmap for counting frequency of characters in a string
#dict can only stores the unique keys and immutable/hashable datatypes only used as a key 
#we generally deserialize the json format to the dict type at the backend so we can 
#access the data by referening to the key of the parsed dict from json


#SET
#set is a collection of unique elements in python 
#set is a mutable datatype the elements in the set can be added or removed at the same
#memory location
#mathematical set operations can be performed on the set
#we use set to remove the duplicates from the data at backend we use set to maintain 
#a perfect uniqueness

#  TASK - E

# APPROACHES:
#1. for removing duplicates we use the set approach which will not accept duplicates to 
# be inserted into set -- time complexity O(n)
#2. calculate the maximum sum of any contiguous window of size k we use the 
# sliding window approach which will calculate the sum of first k elements and 
# then slide the window to next element and add the next element and remove the 
# first element from the sum -- time complexity O(n)

#3. debugging
#problem: when else block placed inside the loops after if condition the else block can be 
#executed for each iterable so it can print not found when there is a missmatch with
#current element 
#solution: it supposed to be after the for block so else block only executes after all
#iterations
