#!/usr/bin/env python3
##Anthony Miklos
##COP2002.C02
##pig latin

##remove extra characters/punctuation
##turn all text to lowercase

##If the word starts with a consonant, move all of the consonants that
##appear before the first vowel to the end of the word, then add ay to the
##end of the word.

##If the word starts with a vowel, just add wayto the end of the word.

##If a word starts with the letter y, the y should be treated as a consonant.
##If the y appears anywhere else in the word, it should be treated as a vowel.

import re

##Main
def main():
    again = "y"
    while again.lower() == "y":
        in_display()
        user_input()
        print()
        again = input("Continue? (y/n): ")
        print()

# initial display
def in_display():
    a = "pig latin translator"
    print(a.title(), end="\n\n\n")

# Get user input str call input sorting function
def user_input():
    text = input(str("Enter text: ")).lower()
    text_cleaned = re.sub(r"[^\w\s]", '', text)
    print("English:    " + text_cleaned)
    words = text_cleaned.split(" ")
    print("Pig Latin: ", end="")
    for word in words:
        print(to_pig_latin(word), end=" ")
        #print()

#function for vowels
def vowel(word):
    return word + "way"

#function for the letter "Y" only if apearing first in the word
def isity(word):
    word = word[1:] + word[0]
    char = word[0]
    while (char not in ["a", "e", "i", "o", "u", "y"]):
        word = word[1:] + char
        char = word[0]
    return word + "ay"

#function for consanants
def cons(word):
    char = word[0]
    while (char not in ["a", "e", "i", "o", "u", "y"]):
        word = word[1:] + char
        char = word[0]
    return word + "ay"

#sort the input and send to corrosponding function
def to_pig_latin(word):
    char = word[0]
    if (char in ["a", "e", "i", "o", "u"]):
        return vowel(word)
    elif (char == "y"):
        return isity(word)
    else:
        return cons(word)
    return word

if __name__ == "__main__":
    main()
