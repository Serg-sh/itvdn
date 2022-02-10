class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.__user_type = user_type

    def access_database(self):
        if self.__user_type != "superuser":
            print("access denied")
        else:
            print("access granted")


class SuperUser(User):
    pass


user = User(name="user", age=30, user_type="user")
su = SuperUser(name="su", age=35, user_type="superuser")

user.access_database()
su.access_database()
