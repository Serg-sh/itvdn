class User:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.__user_type = "user"

    @staticmethod
    def access_database():
        print("access denied")


class SuperUser(User):
    __user_type = "superuser"

    def access_database(self):
        print("access granted")


user = User(name="user", age=30)
su = SuperUser(name="su", age=35)

def show_access(obj):
    obj.access_database()

show_access(user)
show_access(su)
