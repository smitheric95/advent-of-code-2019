import csv 
import itertools

if __name__ == "__main__":
    org_program = []

    with open('input1.csv') as f:
        org_program = [int(j) for i in list(csv.reader(f)) for j in i]
    
    for noun, verb in itertools.product(range(100), repeat=2):
        program = org_program.copy()
        program[1] = noun
        program[2] = verb

        i = 0
        while i < len(program):
            if program[i] == 1:
                program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            elif program[i] == 2:
                program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            else:    
                break

            i += 4

        if program[0] == 19690720:
            print(noun, verb)
            break
