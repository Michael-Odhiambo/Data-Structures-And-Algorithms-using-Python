

class StudentFileReader :

    def __init__( self, inputSrc ) :
        self._inputSrc = inputSrc
        self._inputFile = None

    # Opens the given input file.
    def open( self ) :
        self._inputFile = open( self._inputSrc, "r" )

    # Closes the given input file after reading is done.
    def close( self ) :
        self._inputFile.close()
        self._inputFile = None

    # Gets all the records from the input file.
    def fetchAll( self ) :
        theRecords = list()
        student = self.fetchRecord()

        while student != None :
            theRecords.append( student )
            student = self.fetchRecord()

        return theRecords

    # Same as the fetchAll() method except it gets an individual record.
    def fetchRecord( self ) :
        # Read the first line of the input file.
        line = self._inputFile.readline()
        records = line.split(',')

        if line == '' :
            return None

        # If there is another record, Create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int( records[0] )
        student.firstName = records[1]
        student.lastName = records[2]
        student.classCode = int( records[3] )
        student.gpa = float( records[4] )

        return student



# Storage class.

class StudentRecord :
    def __init__( self ) :

        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0



