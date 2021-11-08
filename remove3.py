"""
Please write a program that reads some text from the keyboard and then deletes every third character (starting with the third).
The remaining characters should be printed on the screen.

Example:

    Enter text: To be or not to be...
    Tobeorno t b..
"""

# Your code here
text = input('Enter a text: ')

out = []

for i in range(0, len(text)):
    if (i + 1) % 3 != 0:
        out.append(text[i])

for i in range(0, len(out)):
    print(out[i], end='')
