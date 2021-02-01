"""

input: Hello, world!    output: 6
input: Hello there, I am a string   output: 13
input: Can you figure out the solution to this puzzle?  output: 23 
input: You can do it! I believe in you!     output: 16


So basically you find the length / 2 of the string to
man i was spliting and counting spaces, then splice the string to that index LOL


"""
import math


input_str = input()

# math.ceil(-23.11) :  -23.0
# math.ceil(300.16) :  301.0
# math.ceil(300.72) :  301.0

# Vs

# math.floor(-23.11) :  -24.0
# math.floor(300.16) :  300.0
# math.floor(300.72) :  300.0

print(math.ceil((len(input_str)-1)/2))





