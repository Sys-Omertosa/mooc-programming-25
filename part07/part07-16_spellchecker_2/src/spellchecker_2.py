from collections import defaultdict
from difflib import get_close_matches

word_dict = defaultdict(set)
with open("wordlist.txt") as words_file:
    for word in words_file:
        word = word.strip()
        word_dict[word[0]].add(word)

text = input("Write text: ")
misspelled = set()
words = text.lower().split()
for word in words:
    if word not in word_dict[word[0]]:
        misspelled.add(word)
        text = text.replace(word, "*" + word + "*")
print(text)
if len(misspelled) > 0:
    print("suggestions:")
    for word in misspelled:
        print(f"{word}: {", ".join(get_close_matches(word, [words for sets in word_dict.values() for words in sets]))}")