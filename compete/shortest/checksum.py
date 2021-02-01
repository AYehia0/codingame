""" 


A checksum is a short sequence of data for checking the integrity of a larger data.
There are different algorithms for doing this. In our case, we are going to use a basic one called Longitudinal redundancy check.

Your work will be to check if the given data is corrupt or not with the checksum passed by.

LRC takes the sum of ascii values of all characters, flips all its bits, adds 1, and outputs the result mod 256.

Example of LRC application with "ABC" :
^ (Bitwise xor)
& (Bitwise and)

'A'=65, 'B'=66, 'C'=67 (ASCII)

(65+66+67)&255=198

198^255 = 57
57+1 = 58
58&255 = 58

Checksum with lrc of 'ABC' = 58
Input
>message to check.
>checksum of the original data.
Output
>Valid or Corrupt if the checksum is correct or not.
Constraints
0 < message "length" < 1000

Example
Input

ABC
58

Output
Valid


SKILLS: map function ,, == inside the list


"""

message = "ABC"
is_valid = 58

sum_ords = 0

for letter in message:
    sum_ords += ord(letter)

if is_valid == ((sum_ords&255)^255) + 1:
    print("valid")
else:
    print("corupted")

# For validation
print(  ((sum(map(ord, message))^255) +1) %256  )
print( ((sum_ords&255)^255) + 1 )



#shortest code
print(["Corrupt","Valid"][((sum(map(ord,input()))&255)^255)+1==int(input())])
#print(["Corrupt","Valid"][((sum(map(ord,input()))^255)+1)%256==int(input())])

