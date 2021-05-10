import numpy as np
import zipfile

from inputPacket import input_students_info
std_num = input_students_info.input_Student_numb()
std_info = input_students_info.input_Student_info(std_num)

from inputPacket import input_courses_info
course_num = input_courses_info.input_Course_numb()
course_info = input_courses_info.input_Course_info(course_num)

from listPacket import list_info
liststd = list_info.list_std(std_info)
listc = list_info.list_Course(course_info)

from markPacket import input_Mark
mark = input_Mark.input_Marks(course_info,std_info)

with zipfile.ZipFile('students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as myzip:
    myzip.write("student.txt")
    myzip.write("courses.txt")
    myzip.write("marks.txt")