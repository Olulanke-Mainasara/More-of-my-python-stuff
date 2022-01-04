def main():
    studlist = []
    studnum = int(input("Enter the number of students captured: "))
    readattendance = open("Attendance.txt", "r")
    studrec = readattendance.readline()

    while studrec != " ":
        studrec = studrec.strip("\n")
        studlist = studrec.split("\t")
        studsum = 0
        for j in range(3,7):
            studsum += int(studlist[j])
            studPercent = (studsum/4) * 100
        print("Your attendance for these days are: ",studPercent)

        break


main()