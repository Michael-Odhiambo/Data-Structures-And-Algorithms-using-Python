
from studentFileReader import StudentFileReader
from studentFileWriterToFile import StudentFileWriter

FILE_NAME = "C:\\Users\\user\\Desktop\\students1.txt"
myReader = StudentFileReader( FILE_NAME ) 
myReader.open()
theRecords = myReader.fetchAll()
myReader.close()

FILE_NAME2 = "C:\\Users\\user\\Desktop\\mystudents.txt"
myWriter = StudentFileWriter( FILE_NAME2 )
myWriter.open()

for record in theRecords :
    myWriter.Write( record.idNum )
    myWriter.Write( record.firstName )
    myWriter.Write( record.lastName )
    myWriter.Write( record.classCode )
    myWriter.Write( record.gpa )

myWriter.close()
