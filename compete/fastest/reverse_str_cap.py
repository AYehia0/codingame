"""
Something easy shit?
tihs ysae Gnihtemos?

"""

sentence = input()


# print(sentence[:len(sentence)-1:][::-1].title()+sentence[-1])
# print(''.join(reversed(sentence[:len(sentence)])))

ans = []
for i in sentence[:len(sentence)-1].split():
    if i.capitalize() == i:
        ans.append(i[::-1].capitalize())
    else:
        ans.append(i[::-1])


print( ' '.join(ans[::-1]) + sentence[-1])


