class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"User: {self.username}"

class Manager(User):
    def manage(self):
        return f"{self.username} is managing the chat."

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender}: {self.content}"

if __name__ == "__main__":
    user = User("alice")
    manager = Manager("bob")
    msg = Message(user.username, "Hello!")
    print(user)
    print(manager.manage())
    print(msg)