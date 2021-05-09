#!/usr/bin/env python

def input_Course_numb():
    n= int(input("Enter number of courses: "))
    return n

def input_Course_info(count):
    namec=[]
    idc=[]
    credit = []
    with open("courses.txt", "w") as f:
        f.write("-----Course List-----\n")
        f.write("Course \t \t ID \t \t Credits\n")
        for n in range(1, count+1):
            print(f"Info of course # {n} ")
            name = input(" -Name: ")
            f.write(name + "\t \t \t")
            namec += [name]
            id = input(" -ID: ")
            f.write(id + "\t \t \t")
            idc += [id]
            cre = input(" -Credits: ")
            f.write(cre + "\n")
            credit += [cre]
    return [namec, idc, credit]
