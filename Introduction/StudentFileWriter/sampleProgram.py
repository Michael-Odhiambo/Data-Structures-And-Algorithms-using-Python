
from studentFileReader import StudentFileReader
from studentFileWriterToTerminal import StudentFileWriter

FILE_NAME = "C:\\Users\\user\\Desktop\\students1.txt"
myReader = StudentFileReader( FILE_NAME ) 
myReader.open()
theRecords = myReader.fetchAll()
myReader.close()

myWriter = StudentFileWriter( theRecords )
myWriter.display()