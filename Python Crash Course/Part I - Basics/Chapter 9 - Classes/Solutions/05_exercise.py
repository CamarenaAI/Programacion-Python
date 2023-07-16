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

user = User('alonso', 'camarena', 'camarenaai', 'ai_dev@python.org', 'mexico')
user.describe_user()
user.greet_user()

print(f"\nNumber of attemps: {user.login_attemps}")

user.increment_login_attemps()
print(f"Number of attemps: {user.login_attemps}")

user.increment_login_attemps()
print(f"Number of attemps: {user.login_attemps}")

user.increment_login_attemps()
print(f"Number of attemps: {user.login_attemps}")

user.increment_login_attemps()
print(f"Number of attemps: {user.login_attemps}")

user.reset_login_attemps()
print(f"Reset the number of attemps")
print(f"Number of attemps: {user.login_attemps}")