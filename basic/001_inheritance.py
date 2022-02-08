class Cat:
    def __init__(self, color, cat_type):
        self.size = "undefined"
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"


class Tiger(Cat):
    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"


cat1 = Cat(color="black", cat_type="Pantera")
cat2 = Cat(color="white", cat_type="indoor")

print(cat1.size)
cat1.set_size()
print(cat1.size)

print(cat2.size)
cat2.set_size()
print(cat2.size)

tiger = Tiger(color="brindle", cat_type="wild")
tiger.set_size()
print(f"{tiger.size=}, {tiger.color=}")
