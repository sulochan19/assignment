# 2. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):

    if word==word[::-1]:
        print("palindrome")
    else:
        print("not palindrome")

word=input("enter the word")
is_palindrome(word)