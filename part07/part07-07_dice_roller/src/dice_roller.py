from random import choice

def roll(die):
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    if die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    if die == "C":
        return choice([1, 4, 4, 4, 4, 4])

def play(die1, die2, times):
    die1_wins = 0
    die2_wins = 0
    for i in range(times):
        die1_num = roll(die1)
        die2_num = roll(die2)
        if die1_num > die2_num:
            die1_wins += 1
        elif die2_num > die1_num:
            die2_wins += 1

    return die1_wins, die2_wins, times - die1_wins - die2_wins

for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")
print()
result = play("A", "C", 1000)
print(result)
result = play("C", "C", 1000)
print(result)