class Employee():

    def __init__(self, id=1, firstname="admin", lastname="admin", email="admin@gmail.com", location="Belgium"):
        self.id = id
        self.firsname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location

    def getFirstname(self):
        return self.firsname
    
    def getLastname(self):
        return self.lastname
    
    def getEmail(self):
        return self.email
    
    def getLocation(self):
        return self.location
    
    def setFirstname(self, newFirstname):
        self.firsname = newFirstname
    
    def setLastname(self, newLastname):
        self.lastname = newLastname
    
    def setEmail(self, newEmail):
        self.email = newEmail
    
    def setLocation(self, newLocation):
        self.location = newLocation