class missingCRF:
    # constructor:
    def __init__(self, tutorName, sessionTime, tutorEmail):
        self.tutorName = tutorName
        self.sessionTime = sessionTime
        self.tutorEmail = tutorEmail

    def printInfo(self):
        print("Name: "+self.tutorName+"; time: " +
              self.sessionTime+"; email: "+self.tutorEmail)

    