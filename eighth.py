class User():
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
    def represent(self, name, mail):
        return f"Hello, dear user! \nYour username is {name}\nYour email address is {mail}"
name = input("Input your username: \n")
fl = False
while fl == False:
    mail = input("input your email:\n")
    if not("@" in mail):
        print("Wrong email. Try again.")
    else:
        fl = True
q = User(name, mail)
print(q.represent(name, mail))


