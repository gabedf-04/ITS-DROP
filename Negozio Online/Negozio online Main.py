class Utente:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password

    def SetUsername(self, username):
        self.username = username
    def SetEmail(self, email):
        self.email = email
    def SetPassword(self, password):
        self.password = password




