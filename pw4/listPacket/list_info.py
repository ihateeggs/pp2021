#!/usr/bin/env python

def list_std(stdinfo):
    print("List of students info: ")
    for i in range (0, len(stdinfo[0])):
        print(f"{i+1}. - \t {stdinfo[0][i]} \t {stdinfo[1][i]} \t {stdinfo[2][i]}")

def list_Course(coursesinfo):
    print("List of courses info: ")
    for n in range (0, len(coursesinfo[0])):
        print(f"{n+1}. - \t {coursesinfo[0][n]} \t {coursesinfo[1][n]}")
    print("--------------\n")