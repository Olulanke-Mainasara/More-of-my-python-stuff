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



