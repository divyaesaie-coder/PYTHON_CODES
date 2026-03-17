#Question:Program to check palindrome,anagram and to count character frequency.
word=input("Enter the word to check palindrome:")
reverse=""
for ch in word:
    reverse=ch+reverse
if reverse==word:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
#FINDING ANAGRAM
a=input("ENTER A WORD TO CHECK ANAGRAM:")
b=input("ENTER A WORD TO CHECK ANAGRAM")
if sorted(a)==sorted(b):
    print("ANAGRAM")
else:
    print("NOT A ANAGRAM")
#COUNTING ALPHAHBETS
from collections import Counter
print(Counter(input("ENTER A WORD OR SENTENCE TO COUNT ALPHABETS:")))
