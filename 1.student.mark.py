#!/usr/bin/env python
# coding utf-8

# In[15]:


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

def list_std(stdinfo):
    print("List of students info: ")
    for i in range (0, len(stdinfo[0])):
        print(f"{i}. - \t {stdinfo[0][i]} \t {stdinfo[1][i]} \t {stdinfo[2][i]}")

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

def list_Course(coursesinfo):
    print("List of courses info: ")
    for n in range (0, len(coursesinfo[0])):
        print(f"{n+1}. - \t {coursesinfo[0][n]} \t {coursesinfo[1][n]}")
    print("--------------\n")

def input_Marks(coursesinfo,stdinfo):
    marks=[]
    print("Please select a course (#) from below: ")
    for n in range (0, len(coursesinfo[0])):
        print(f"{n+1}. - \t {coursesinfo[0][n]} \t {coursesinfo[1][n]}")
    cidx = int(input("Please select a course: "))
    cid = coursesinfo[0][cidx-1]

    for i in range (0, len(stdinfo[0])):
        print(f"{i+1}. - \t {stdinfo[0][i]} \t {stdinfo[1][i]} \t {stdinfo[2][i]}")
        sid = stdinfo[0][i]
        mark = int(input(f"The mark of student {sid}:"))
        marks += [(cid,sid,mark)]
    print(f"The mark of students in " + coursesinfo[0][cidx-1] + f" is:" )
    return marks



stdCount = input_Student_numb()
print(f"Enter information for {stdCount} student(s): ")
stdinfo = input_Student_info(stdCount)
print(stdinfo)

courseCount=input_Course_numb()
courses_info = input_Course_info(courseCount)
print(courses_info)

list_std(stdinfo)

list_Course(courses_info)

marks = input_Marks(courses_info,stdinfo)
print(marks)


