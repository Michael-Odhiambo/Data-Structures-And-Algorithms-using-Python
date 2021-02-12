
# To illustrate the use of a 2-D array, suppose we have a collection of exam grades stored in a text file for
# a group of students that we need to process. For example, we may want to compute the average exam grade for
# each student or the average grade for each exam, or both. A sample file is provided below. The file contains
# the grades for multiple students, each of whom have grades for multiple exams. The first line indicates the
# number of exams for which each student has a grade. The remaining lines contain the actual exam grades. Each
# line contains the grade for an individual student, with the grades listed in exam order.

# Since we have multiple grades for multiple students, we can store the grades in a 2-D array in which each
# row contains the grades for an individual student and each column contains the grades for a given exam.

from array2D import Array2D

fileName = "C:\\Users\\user\\Desktop\\studentsExams.txt"

# Open the text file for reading.
gradeFile = open( fileName, "r")

# Extract the first two values which indicate the size of the array.
numExams = int( gradeFile.readline() )
numStudents = int( gradeFile.readline() )

# Create the 2-D array to store the grades.
examGrades = Array2D( numStudents, numExams )

# Extract the grades from the remaining lines.
i = 0
for student in gradeFile :
    grades = student.split()
    print( grades )
    for j in range( numExams ) :
        examGrades[ i, j ] = int( grades[j] )
    i += 1

# Close the text file.
gradeFile.close()


# With the grades extracted from the file and stored in the 2-D array, we can now process the grades as needed.
# Suppose we want to compute and display each student's exam grade, which we can do with the following code:

# Compute each student's average exam grade.
for i in range( numStudents ) :
    # Tally the exam grades for the ith student.
    total = 0
    for j in range( numExams ) :
        total += examGrades[ i, j ]

# Compute the average for the ith student.
examAvg = total / numExams
print( "%2d:  %6.2f" % ( i + 1, examAvg) )
