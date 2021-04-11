#!/usr/bin/env python
# coding utf-8

# In[15]:

class Student:
    def __init__(self, n="", id = "", d = ""):
        self._name = n
        self._stdid = id
        self._dob = d

    def getname(self):
        return self._name

    def getid(self):
        return self._stdid

    def getdob(self):
        return self._dob

    def input(self):
        self._name = input(f"\t - Enter student name: ")
        self._stdid = input(f"\t - Enter student ID : ")
        self._dob = input(f"\t - Enter student DOB: ")
        return print(f"Student Info: \t{self._name} \t {self._stdid} \t {self._dob} \n ----------"  )

    def __str__(self):
        return  f" \t - Student Name: {self._name}" \
                f" \t - Student ID: {self._stdid}" \
                f" \t - Student DOB: {self._dob}"

    def describe(self):
        print(self.__str__())

class Course:
    def __init__(self, cn="", cid=""):
        self._course_name = cn
        self._course_id = cid

    def getcoursename(self):
        return self._course_name

    def getcourseid(self):
        return self._course_id

    def input_course(self):
        self._course_name = input("\t - Course name: ")
        self._course_id = input("\t - Course ID: ")
        return print(f"Course info:  {self._course_name} \t {self._course_id} \n ----------")

    def __str__(self):
        return f" \t - Course name: {self._course_name}" \
               f" \t - Course ID: {self._course_id}"

    def describec(self):
        print(self.__str__())

class Mark:
    def __init__(self, student, course, mark = 0):
        self._student = student
        self._course = course
        self._mark = mark

    def input_mark(self):
        self._mark = input(f" \t - Enter mark for student {self._student.getname()} in course {self._course.getcourse()}: ")

    def __str__(self):
        return f"Mark of student {self._student.getname()} in course {self._course.getcoursename()}: {self._mark} "

    def describem(self):
        print(self.__str__())

class Management:
    def list(self):
        pass

    def input(self):
        pass

class Student_Mana(Management):
    def __init__(self):
        self._stds = []
        self._cs = []
        self._marks = []

    def getStudents(self):
        return self._stds[i]

    def getCourse(self):
        return  self._cs[i]

    def getMark(self):
        return self._marks[i]

    def inputSudent(self):
        std = Student()
        std.input()
        self._stds += [std]

    def inputCourse(self):
        c = Course()
        c.input_course()
        self._cs += [c]

    def inputMark(self):
        for i in range(len(self._stds)):
            m = []
            for j in range(len(self._cs)):
                c = int(input(
                    f" \t -Enter mark of student name {self._stds[i].getname()} in course {self._cs[j].getcoursename()}: "))
                m += [c]
            self._marks += [m]

    def listMark(self):
        for i in range(len(self._stds)):
            for j in range(len(self._cs)):
                print(f"Student {self._stds[i].getname()} gets {self._marks[i][j]} in course {self._cs[j].getcoursename()}")


numofStudents = int(input(" - Enter number of students: "))
sm = Student_Mana()
for i in range (0, numofStudents):
    sm.inputSudent()

numofCourses = i = int(input(" - Enter number of courses: "))
courses = []
mark =  []
for i in range (0, numofCourses):
    sm.inputCourse()
sm.inputMark()
print("\n")
sm.listMark()



