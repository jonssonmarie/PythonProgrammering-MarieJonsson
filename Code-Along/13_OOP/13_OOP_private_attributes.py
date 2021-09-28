""" Private attributes"""

class Patient:
    def __init__(self, name, diagnosis) -> None:
        self.name = name
        self.__diagnosis = diagnosis

    def __repr__(self) -> str:
        return f"Patient{self.name}, {self.__diagnosis}"

p1 = Patient(" Gore", "Migraine")  # object
print(p1)

p1.name = " Greta"
print(p1)

# try to change __diagnosis
p1.__diagnoisis = "cold"  # will not change diagnosis due to __

print(p1)
print(p1.__dict__)
# Python does name mangling __:> changes __diagnisis to _Patient__diagnosis
# Python skapar alltså en _diagnosis också

# Kolla upp name mangling !