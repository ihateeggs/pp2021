#!/usr/bin/env python

def input_Student_numb():
    i= int(input("Enter number of students: "))
    return i

def input_Student_info(count):
    ids=[]
    names=[]
    dobs=[]
    for i in range(1, count+1):
        print(f"Info of student # {i} ")
        name = input(" -Name: ")
        names += [name]
        id = input(" -ID: ")
        ids += [id]
        from datetime import datetime
        dob = input(" -DOB(DD/MM/YYYY): ")
        dob = datetime.strptime(dob, '%d/%m/%Y')
        print(f'Day: {dob.day}')
        print(f'Month: {dob.month}')
        print(f'Year: {dob.year}')
        dobs += [dob]
    return [names, ids, dobs]