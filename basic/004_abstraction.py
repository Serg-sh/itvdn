class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __str__(self):
        text = (f"{self.country=}",
                f"{self.name=}",
                f"{self.age=}",
                f"{self.gender=}",
                f"{self.height=}",
                f"{self.weight=}")
        return ("\n").join(text)


class Database:
    def __init__(self):
        self.__elements = []

    def read_database(self, criteria: dict):
        elements = []
        for elem in self.__elements:
            if self.__check_criteria(elem, criteria):
                elements.append(elem)

        return elements

    def write_data(self, element: Data, *args):
        self.__elements.append(element)
        self.__elements.extend(args)

    @staticmethod
    def __check_criteria(data: Data, criteria: dict):
        name, _ = tuple(criteria.items())[0]
        return data.__dict__.get(name) == criteria.get(name)


def main():
    db = Database()
    data1 = Data("ua", "Serg", 39, "male", 173, 73)
    data2 = Data("uk", "John", 39, "male", 183, 80)
    db.write_data(data1, data2)

    for element in db.read_database({"country": "uk"}):
        print(element)
        print("=" * 10)


if __name__ == '__main__':
    main()
