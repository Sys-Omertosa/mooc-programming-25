def no_vowels(text : str) -> str:
    vowels = "aeiou"
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text

if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))