# index->layer number, element->highest letter in layer
letter_array = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layers = int(input("Layers: "))

line = letter_array[layers] * (2 * layers - 1)
print(line)

for i in range(layers-1, 0, -1):
    line = line[:layers-i] + (letter_array[i] * (2 * i - 1)) + line[layers+i-1:]
    print(line)

for i in range(2, layers+1):
    line = line[:layers-i] + (letter_array[i] * (2 * i - 1)) + line[layers+i-1:]
    print(line)