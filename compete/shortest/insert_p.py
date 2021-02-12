"""
shit i forgot to scrape lol

"""


l = [ "A", "E", "I", "O", "U"]
s = ""
string = input()

for char in string:
    if char.upper() in l:
        s += char + 'p' + char
    else:
        s += char

print(s)

