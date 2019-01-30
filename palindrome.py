import logging

word = input("enter the word")
if word.isalpha():
   Flag= True

else:
    Flag= False
    print("Please enter only alphabets")
    exit()

word10= word[::-1]
if word10 == word:
    print ("word is palindrome")

else:
    print ("not a palindrome")
    print(logging.info(""))


