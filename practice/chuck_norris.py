message = input()

message_bin = [format(j, '07b') for j in [ord(i) for i in message]]

to_encode = ''.join(message_bin)


# print(to_encode)
ans = []

# i will do it the non-pythonic way,,, later 
for k, group in itertools.groupby(to_encode):

    if k == '1':
        x = f"0 {'0'*len(list(group))} "
    else:
        x = f"00 {'0'*len(list(group))} "

    ans.append(x)


# Stupid way to do this 
print(''.join(ans).rstrip(' '))
