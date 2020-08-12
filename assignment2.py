


class user:
    name = 'Barbara Ann'
    email = 'barbara.ann@gmail.com '
    password = '12345678'
    account = 0

    def login(self):
        entry_email = input("enter your email:")
        entry_password = input("enter you password:")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(self.name))
        else:
            print("you are not authorized for this page.")





new_user = user("Barbara Ann","barbara.ann@gmail.com","password", 0)




class employee(user):
        title = clerk
        department = 'General'

class customer(user):
        mailing_address = ' '
        mailing_list = True
        


def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account 
