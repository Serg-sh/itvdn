import math


class Core:
    def __init__(self):
        self.__opperations = {
            "sum": lambda a, b: a + b,
            "diff": lambda a, b: a - b,
            "prod": lambda a, b: a * b,
            "div": lambda a, b: a / b,
            "sqrt": lambda a, _: math.sqrt(a),
            "log": lambda a, b: math.log(a, b),
            "pow": lambda a, b: a ** b,
        }

    def _calculate(self, a, b, op):
        return self.__opperations[op](a, b)

    @property
    def opperations(self):
        return self.__opperations


class Calc(Core):
    def __parse(self, a_b_op: str):
        a, b, op = a_b_op.split(" ")
        return Core()._calculate(a=int(a), b=int(b), op=op)

    @property
    def parse(self):
        return self.__parse


def main():
    value = input(f"Введите 2 числа и операцию из списка: {Core().opperations.keys()} через пробел \n")
    print(Calc().parse(value))


if __name__ == "__main__":
    main()
