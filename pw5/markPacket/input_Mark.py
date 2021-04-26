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
    return marks