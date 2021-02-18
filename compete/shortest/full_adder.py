"""
PROBLEM:
Read two binary numbers, calculate the sum and print the result in binary.

You will not be able to solve 100% of this problem if you do "binary to decimal conversion". You must simulate the full Adder circuit (unless you use BigInt).

FullAdder is a circuit that receives carryIn, bit A and bit B and returns sum and carryOut of the sum. For example: To do A + B with 32 bits, 32 FullAder circuits are placed in sequence. The first FullAdder receives carryIn0 = 0, and the least significant bits of A and B (bitA0 and bitB0), the result is cOut0 and the bit SUM0. The second FullAdder receives carryIn1 = carryOut0, and bits bitA1 and bitB1. The process is repeated until the last FullAdder. Finally, the last carryOut (In this exemple, carryOut31) is added to SUM.

Full Adder Formulas:
sum = (A XOR B) XOR cIn
cOut = ((A XOR B) AND cIn) OR (A AND B)

+------------------------------+
|   Full Adder - Truth Table   |
+-----------------+------------+
|      Input      |   Output   |
+-----+-----+-----+-----+------+
|  A  |  B  | cIn | SUM | cOut |
+-----+-----+-----+-----+------+
|  0  |  0  |  0  |  0  |   0  |
+-----+-----+-----+-----+------+
|  0  |  0  |  1  |  1  |   0  |
+-----+-----+-----+-----+------+
|  0  |  1  |  0  |  1  |   0  |
+-----+-----+-----+-----+------+
|  0  |  1  |  1  |  0  |   1  |
+-----+-----+-----+-----+------+
|  1  |  0  |  0  |  1  |   0  |
+-----+-----+-----+-----+------+
|  1  |  0  |  1  |  0  |   1  |
+-----+-----+-----+-----+------+
|  1  |  1  |  0  |  0  |   1  |
+-----+-----+-----+-----+------+
|  1  |  1  |  1  |  1  |   1  |
+-----+-----+-----+-----+------+

https://lms.matlabhelper.com/course/simulinkfunda-m3c9l1-half-and-full-adder/

A line containing the binary number A
Another line containing the binary number B

A line containing the result of A + B in binary (SUM), don't forget to add the last carry out the sum. If the carry out is not 0.
CONSTRAINS:
1≤ A length === B length ≤ 300
1≤ SUM length ≤ 301
EXAMPLE input:
1010
0101
EXAMPLE output:
1111
------------
1010
0101
1111
1010
1101
10111
100101101011010000100
100110000000100001110
1001011101011110010010
100000000000000000000000000000000000000000000000000000000000000
011111111111111111111111111111111111111111111111111111111111111
111111111111111111111111111111111111111111111111111111111111111
111110110001010101000111001111110111010101101001111011101000001101010100110010111010101000010000011011100001101110100011010111010000100101100110111100001001011111010110011101001101100001101000101010011110110110010111101001000110011001010110101011000000101101001100000010111111110110001001110010001000
101010100010010011011101101110100011001100000001010000000010010100111010111011000001000011011010111010110010001011011000000101110111110010100111111110101111100101101001100110011010000110010100111010111110010001001111110111110011001110010011011000110100010000110011111110110100101001011011001000100101
1101001010011101000100100111110011010100001101011001011101010100010001111101101111011101011101011010110010011111001111011011101001000011000001110111010111001000101000000000011100111100111111101100101011101000111100111100000111001100111101010000011110100111110000000000001110100011111100100111010101101
100010100000110010111000001101110100001000100100001100100101110110110000110100100100010011111110100000001100110100001111011100000001000010100111011110010110111001101111101101010010010011010111111010101111001010001101100011100110100111000011100101100000101111011001101000011001001111100111001011000110
010000011110001010100111111110111010011111100011000010001111111011001111100001100100001101001010011101100101100001110010101110011000000000000011101010100001001111101110110111111110111010110001001110110000010000111011010011000110110000100001111000110110000011000000110001010100110001101000100111111110
110010111110111101100000001100101110101000000111001110110101110010000000010110001000100001001000111101110010010110000010001010011001000010101011001000111000001001011110100101010001001110001001001001011111011011001000110110101101010111100101011110010110110010011010011001101110000001001111110011000100
001100010111110001000000111001001100101000110001110110011101001001001110110010010011010011011011100011001011100111011101101000100110010011110001001000101010001101111011001101001010000001000110110001101101011011011111010110110010011011100011011010001011010011110011010010100101011100000101101110000010
110000100000010001010010111000111101001011000100111101011101110010001010010111000010001100000101110111000011111000101100010010011010011101111110000110000100001000011100001100000000101100100010000011000001000000001100101110001110111000001101110001101001111001110001011000011111111001001000101010110011
111100111000000010010011110010001001110011110110110011111010111011011001001001010101011111100001011010001111100000001001111011000000110001101111001110101110010110010111011001001010101101101000110100101110011011101100000101000001010011110001001011110101001101100100101011000101010101001110011000110101
1
1
10

"""

# another trick to shorten the code is using l(input) as print , which is kinda weird 
l=input
print(f"{int(l(),2)+int(l(),2):b}")
#l((f"{int(l(),2)+int(l(),2):b}"))
