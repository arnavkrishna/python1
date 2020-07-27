
#we can say from ___ import specific function like this -
from functions import square
#then use it -
for i in range(10):
    print(f"the square of {i} is {square(i)}")

# or we can import the whole program and then specify the name of the fuction in the command -
import functions

for i in range(10):
    print(f"the square of {i} is {functions.square(i)}")