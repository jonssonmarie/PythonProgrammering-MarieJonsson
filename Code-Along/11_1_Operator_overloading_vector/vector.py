class Vector:
    """ A class to represent a Euclidean vector with magnitude and direction"""

    def __init__(self, *numbers) -> None:  # * ger valfri mängd numbers
        print(numbers)
        for number in numbers:
            if not isinstance(number, (float,int)):
                raise TypeError(f"{number} must be a float or int not {type(number)}")

        if len(numbers) <= 0:
            raise ValueError("Vectors can't be empty")
        
        self._numbers = tuple(float(number) for number in numbers)

@property
def numbers(self) -> tuple:
    return self._numbers

# (2,3) 0 (1,1,1,) not ok. Check size of vector
def __add__(self, other:"Vector") -> "Vector":
    if self.validate_vectors(other):
        numbers = (a + b for a,b in zip(self.numbers, other.numbers))
        return Vector(*numbers)  # * unpack (som en "split") det som finns i numbers

def __len__(self) -> int:
    """ Returns number of components in a Vector"""
    return len(self.numbers) 

def validate_vectors(self, other:"Vector") -> bool:
    """ validate number of components in a Vector not the Euclidean distance"""
    if not isinstance(other, Vector) or len(other) != len(self):
        raise TypeError("Both must be Vector and same length")
        return len(self) ==  len(other)

def __repr__(self) -> str:
    return f"Vector{self.numbers}"

def __str__(self) -> str:
    return 

