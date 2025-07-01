from collections import defaultdict

word_dict = defaultdict(set)
with open("wordlist.txt") as words_file:
    for word in words_file:
        word = word.strip()
        word_dict[word[0]].add(word)

text = input("Write text: ")
words = text.lower().split()
for word in words:
    if word not in word_dict[word[0]]:
        text = text.replace(word, "*" + word + "*")
print(text)