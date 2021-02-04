n = int(input())
word = input()
print(word[n%len(word):]+word[:n%len(word)])