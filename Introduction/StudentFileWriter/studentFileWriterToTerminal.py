
class StudentFileWriter :

    def __init__( self, theRecords ) :
        self._theRecords = theRecords
    
    def display( self ) :
        for record in self._theRecords :
            print( record.idNum, record.firstName, \
                record.lastName, record.classCode, record.gpa )


