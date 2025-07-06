from string import ascii_letters, punctuation

def separate_characters(my_string):
    ascii_string = ""
    punc_string = ""
    other_string = ""
    for char in my_string:
        if char in ascii_letters:
            ascii_string += char
        elif char in punctuation:
            punc_string += char
        else:
            other_string += char
    return ascii_string, punc_string, other_string

parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])