class User:
    def __init__(self, first_name, last_name, username, email, country):
        self.fn = first_name.title()
        self.ln = last_name.title()
        self.username = username
        self.email = email
        self.country = country.title()
        self.login_attemps = 0

    def describe_user(self):
        print("This profile is from:")
        print(f" {self.fn} {self.ln}\n"
            f" Username: {self.username}\n"
            f" Email: {self.email}\n"
            f" Country: {self.country}\n")

    def greet_user(self):
        print(f"Welcome back, {self.username}. Ready to take a new lesson today")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

class Admin(User):
    def __init__(self, f_name, l_name, username, email, country):
        super().__init__(f_name, l_name, username, email, country)
        self.privileges = []

    def show_privileges(self):
        if self.privileges:
            print(f"The user have this privileges")
            for privilege in self.privileges:
                print(f"- {privilege.title()}" )
        else:
            print(f"The user don't have privileges")

adm = Admin('alonso', 'camarena', 'camarenadev', 'ac_dev@python.org', 'mexico')
adm.privileges = ["can add post", "can delete post", "can ban user"]
adm.describe_user()
adm.show_privileges()

adm = Admin('ismael', 'zamora', 'zamoradev', 'iz_dev@python.org', 'mexico')
adm.privileges = []
adm.describe_user()
adm.show_privileges()