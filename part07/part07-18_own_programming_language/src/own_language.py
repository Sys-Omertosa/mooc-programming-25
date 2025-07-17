from string import ascii_uppercase

def run(program : list[str]) -> list[int]:
    outputs = []

    variables = {}
    for letter in ascii_uppercase:
        variables[letter] = 0

    loc_indexes = {}
    for index, command in enumerate(program):
        if command[-1] == ":":
            loc_indexes[command[:-1]] = index

    index = 0
    while index < len(program):
        parts = program[index].strip().split()
        command_type = parts[0]

        match command_type:
            case "END":
                return outputs
            case "PRINT":
                try:
                    value1 = int(parts[1])
                except ValueError:
                    value1 = variables[parts[1]]
                outputs.append(value1)
            case "MOV" | "ADD" | "SUB" | "MUL":
                try:
                    value2 = int(parts[2])
                except ValueError:
                    value2 = variables[parts[2]]

                match command_type:
                    case "MOV":
                        variables[parts[1]] = value2
                    case "ADD":
                        variables[parts[1]] += value2
                    case "SUB":
                        variables[parts[1]] -= value2
                    case "MUL":
                        variables[parts[1]] *= value2
            case "JUMP":
                index = loc_indexes[parts[1]]
            case "IF":
                try:
                    value1 = int(parts[1])
                except ValueError:
                    value1 = variables[parts[1]]
                try:
                    value2 = int(parts[3])
                except ValueError:
                    value2 = variables[parts[3]]
                if eval(str(value1) + parts[2] + str(value2)):
                    index = loc_indexes[parts[5]]

        index += 1

    return outputs