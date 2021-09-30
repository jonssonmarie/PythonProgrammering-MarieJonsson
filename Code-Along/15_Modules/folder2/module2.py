from sys import path
path.append("folder1")
import module1

def say_hello2():
    print(f"{__name__} says hello")

# want to import say_hello1
"""
from sys import path        # importera module sys och path

path.append("folder1")      # tänk på vilken folder detta script står i för path här räcker det med folder1 

import module1              # importera sedan scriptet
"""