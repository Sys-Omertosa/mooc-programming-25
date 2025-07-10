from random import sample

def words(n, beginning):
    word_pool = set()
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning):
                word_pool.add(line)

    if len(word_pool) < n:
        raise ValueError

    return sample(list(word_pool), n)

word_list = words(3, "ca")
for word in word_list:
    print(word)