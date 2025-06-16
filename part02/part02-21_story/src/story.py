story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == previous_word:
        print(story)
        break

    story += word + " "
    previous_word = word