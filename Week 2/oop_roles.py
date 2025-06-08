class User:
    def __init__(self, name):
        self.name = name

    def action(self):
        raise NotImplementedError

class Intern(User):
    def action(self):
        return f"{self.name} is working on tasks."

class Mentor(User):
    def action(self):
        return f"{self.name} is mentoring interns."

class Admin:
    def log_admin_action(self):
        return "Admin action logged."

class HR:
    def log_hr_action(self):
        return "HR is handling recruitment."

class ComposedUser(User):
    def __init__(self, name, role_obj):
        super().__init__(name)
        self.role_obj = role_obj

    def action(self):
        return f"{self.name}: {self.role_obj.log_admin_action() if hasattr(self.role_obj, 'log_admin_action') else self.role_obj.log_hr_action()}"

if __name__ == "__main__":
    users = [
        Intern("Alice"),
        Mentor("Bob"),
        ComposedUser("Charlie", Admin()),
        ComposedUser("Daisy", HR())
    ]
    for user in users:
        print(user.action())
