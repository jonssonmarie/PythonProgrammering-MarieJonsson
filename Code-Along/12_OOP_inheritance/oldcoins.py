class OldCoinsStash:
    def __init__(self, owner):
        self.owner = owner

        # these attributes are "private" - only allow to access them in the class
        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler, skilling):
        if riksdaler <= 0 or skilling <= 0:
            raise ValueError(
                f"You try to deposit {riksdaler} riksdaler and {skilling} skilling. They have to be positive")

        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, riksdaler, skilling):
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError(
                f"You can't withdraw more than you have in your stash")

        self._riksdaler -= riksdaler
        self._skilling -= skilling

    def check_balance(self):
        return f"Coins in stash: {self._riksdaler} riksdaler, {self._skilling} skilling"

    def __repr__(self):
        return f"OldCoinStash(owner='{self.owner}')"

stash1 = OldCoinsStash("Gore Bord")
print(stash1.check_balance())

try:
    stash1.deposit(-5, 31)  # check if I can rob the stash
except ValueError as err:
    print(err)

print(stash1.check_balance())
stash1.deposit(50, 42)
print(stash1.check_balance())

try:
    stash1.withdraw(500, 31)  # check if I can rob the stash again
except ValueError as err:
    print(err)

print(stash1.check_balance())
stash1.withdraw(25, 20)
print(stash1.check_balance())

# there are ways to rob the stash -> try and see if you can find them :)
# then try to fix this bug (or feature ;) ?)