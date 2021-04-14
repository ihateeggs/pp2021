#!/usr/bin/env python

def input_Course_numb():
    n= int(input("Enter number of courses: "))
    return n

def input_Course_info(count):
    namec=[]
    idc=[]
    for n in range(1, count+1):
        print(f"Info of course # {n} ")
        name = input(" -Name: ")
        namec += [name]
        id = input(" -ID: ")
        idc += [id]
    return [namec, idc]