#!/usr/bin/env python

def input_Course_numb():
    n= int(input("Enter number of courses: "))
    return n

def input_Course_info(count):
    namec=[]
    idc=[]
    credit = []
    for n in range(1, count+1):
        print(f"Info of course # {n} ")
        name = input(" -Name: ")
        f.write(namec + "\n")
        namec += [name]
        id = input(" -ID: ")
        f.write(id + "\n" )
        idc += [id]
        cre = input(" -Credits: ")
        f.write(cre + "\n")
        credit += [cre]
    return [namec, idc, credit]
