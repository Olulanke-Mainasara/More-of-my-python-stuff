studlist = []
readattendance = open("Attendance.txt")
for i in readattendance:
    i = i.rstrip("\n")
    studlist = l.split("\t")
    studsum