def histogram(string):
    string = string.lower()
    frequency = {c: string.count(c) for c in string}

    for char, freq in frequency.items():
        print(f"{char} {'*'*freq}")