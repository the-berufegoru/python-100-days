#!/usr/bin/python

students = ['Mike', 'Jack']


for student in students:
    print(student)
    
print('--------------------------UPDATED LIST--------------------------')
students.append('Amy')
students.append('Calvin')
students.append('Sam')

print(students.__contains__('Sam'))

for student in students:
    print(student)