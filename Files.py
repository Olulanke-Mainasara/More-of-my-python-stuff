# Code 1
def main():
    num_days = int(input("For how many days do you have sales: "))
    sales_file = open("sales.text", "w")

    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for the day #" + str(count) + ": "))
        sales_file.write(str(sales) + "\n")

    sales_file.close()
    print("Data written to sales.txt.")

main()

# Code 2
def main():
    studlist = []
    studnum = int(input("Enter the number of students captured: "))
    readattendance = open('Attendance.txt', 'r')

    for i in range(studnum):
        studrec = readattendance.readline()
        studlist = studrec.split('\t')
        studsum = 0
        for j in range(3,7):
            studsum += int(studlist[j])
            studPercent = (studsum/4) * 100
        print("Your attendance for these days are: ",studPercent)

main()

# Code 3
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

# Code 4
def main():
    numberOfStudents  = int(input("Enter the number of students: "))
    AttendanceFile = open('Attendance.txt','w')

    for counter in range(1, numberOfStudents+1):
        First_name = input("Enter the first name for student #" + str(counter) + ': ')
        AttendanceFile.write(First_name + '\t')

        Last_Name = input("Enter the last name for student #" + str(counter) + ': ')
        AttendanceFile.write(Last_Name + '\t')

        Matric_Number = int(input("Enter the matric number for student #" + str(counter) + ': '))
        AttendanceFile.write(str(Matric_Number) + '\t')


        MAR04_Attendance = int(input("Enter the attendance for March 4th for student #" + str(counter) + ': '))
        AttendanceFile.write(str(MAR04_Attendance) + '\t')

        MAR11_Attendance = int(input("Enter the attendance for March 11th for student #" + str(counter) + ': '))
        AttendanceFile.write(str(MAR11_Attendance) + '\t')

        MAR18_Attendance = int(input("Enter the attendance for March 18th for student #" + str(counter) + ': '))
        AttendanceFile.write(str(MAR18_Attendance) + '\t')

        MAR25_Attendance = int(input("Enter the attendance for March 25th for student #" + str(counter) + ': '))
        AttendanceFile.write(str(MAR25_Attendance) + '\t' + '\n' )


    AttendanceFile.close()
    print("Data captured!")

main()



