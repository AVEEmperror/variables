﻿"""
Please write a program that reads a line of text, and then prints the most frequent letter in it. The program should ignore case,
and the most frequent letter should be capitalized. If there is more than one letter that appears most frequently, it is enough
to print any of them. (for those of you who are ambitious: in such case, write down all the letters that appear most of the times,
each in a separate line)

Example:

    Write the text: To be or not to be
    O

In the advanced version:

    Enter text: Abba
    A
    B

Tip: I suggest creating a dictionary that stores for each letter the number of its occurrences. The number of occurrences of
a given letter can be found using the `count` method for a text string (please search for its documentation yourself).
"""

# Your code here

text = input('Enter a text: ').lower()
seen = []
data = {}

for i in range(0, len(text)):
    if text[i] in seen:
        continue
    data[text[i].upper()] = text.count(text[i])
    seen.append(text[i])

data_sorted = sorted(data.items(), key = lambda data_t:data_t[1], reverse = True)
print(data_sorted[0][0])

for i in range(1, len(data_sorted)):
    if data_sorted[i][1] == data_sorted[0][1]:
        print(data_sorted[i][0])



