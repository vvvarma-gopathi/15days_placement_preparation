# Task - A
def first_non_repeating(text):
    d={}
    for i in text:
        if i == ' ':
            continue
        d[i]=d.get(i,0)+1
    for key,value in d.items():
        if value ==1:
            return key
    return -1


print(first_non_repeating('aapple'))
print(first_non_repeating('seconds'))
print(first_non_repeating('in incline'))
print(first_non_repeating('at the top'))
print(first_non_repeating('all are well'))


#TASK - B


#list 
#list is an dynamic array in python which stores multiple values
# in consicutive memory locations list is a mutable datatype which can be 
#manipulated or can be changed

print('='*25,'list example','='*25)

lst=[1,2,3]
lst.append(4)
print(lst)
lst.append([6,8])
print(lst)

print('='*25,'tuple example','='*25)
#tuple is ordered collection which is immutable datatype in python which
#cannot be manipulated or changed it is perticularly used when the 
#values are fixed or not supposed to change

t=(1,2,3)
print(t[0])

print('='*25,'set example','='*25)
#set is a unique element collection which doesnt have duplicate values in it
#set is a mutable datatype since we can remove or add elements but cannot update values
#set has no indexing the elements are not fixed in a position
#mathematical set operations can be performed on the set

s={1,2,3,4,6,8}
s.add(7)
print(s,'after adding 7')
s.add(1)
print(s,'after adding 1 second time')

print('='*25,'dictionary example','='*25)
#dictionary is a key value pair collection which is a mutable datatype in python
#the keys of the dictionary should be unique and hashable, mutable datatypes cannot be 
#used as a dictionary keys 

student = {'name':"varma","age":22,"grade":"A+"}
print(student,type(student))
print(student.get("marks",100))


#TASK - C
def find_student(student):
    students = ["Ravi", "Anil", "Kiran", "Suresh"]
    for student in students:
        if student == student:
            return 'Kiran is found in students'
    return 'kiran is not found in students'

print(find_student('Kiran'))
print(find_student('Anil'))
print(find_student('Ravi'))

#Task - D

#What I Learned:
#Data types, loops, conditional statements, mutable vs immutable, variables and operators
#functions, keyword arguments and arguements

#difficult : no difficulties

