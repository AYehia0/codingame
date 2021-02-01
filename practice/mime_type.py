elements = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    elements[ext.lower()] = mt

# print(elements) 
for i in range(q):
    fname = input()
    # if there is no dot in the filename --> it's invalid name : print UNKNOWN
    if not '.' in fname:
        print("UNKNOWN")
        continue
    name = fname.split('.')[-1].lower()

    # If the name in the dict
    if elements.get(name):
        print(elements[name])
    else:
        print('UNKNOWN')
