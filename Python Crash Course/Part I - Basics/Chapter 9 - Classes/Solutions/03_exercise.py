class User:
    def __init__(self, first_name, last_name, username, email, country):
        self.fn = first_name.title()
        self.ln = last_name.title()
        self.username = username
        self.email = email
        self.country = country.title()

    def describe_user(self):
        print("This profile is from:")
        print(f" {self.fn} {self.ln}\n"
            f" Username: {self.username}\n"
            f" Email: {self.email}\n"
            f" Country: {self.country}\n")

    def greet_user(self):
        print(f"Welcome back, {self.username}. Ready to take a new lesson today")

user = User('alonso', 'camarena', 'camarenaai', 'ai_dev@python.org', 'mexico')
user.describe_user()
user.greet_user()