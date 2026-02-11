class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayName(self,):
        return self.first_name

    def saySecondName(self):
        return self.last_name

    def sayAllName(self):
        return self.first_name + ' ' + self.last_name
