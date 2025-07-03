def filter_incorrect():
    correct_lines = []
    with open("lottery_numbers.csv") as file:
        for line in file:
            try:
                line = line.strip()
                parts = line.split(";")
                week_number = int(parts[0].split()[1])
                numbers = {num for num in map(int, parts[1].split(",")) if 1 <= num <= 39}
                if len(numbers) < 7:
                    continue
                correct_lines.append(line)
            except:
                pass

    with open("correct_numbers.csv", "w") as file:
        for line in correct_lines:
            file.write(line + "\n")

filter_incorrect()