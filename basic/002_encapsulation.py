class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = self.__valid_age(age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = User.__valid_age(age)

    @staticmethod
    def __valid_age(age):
        if isinstance(age, int) and age > 0:
            return age
        else:
            return -1


user1 = User(name="alex", age=30)
print(user1.name, user1.age)
user1.age = "20"
print(user1.name, user1.age)
user1.age = -20
user1.name = "Bob"
print(user1.name, user1.age)
user1.age = 20.5
print(user1.name, user1.age)
user1.age = 25
user1.name = "Johnny"
print(user1.name, user1.age)
