#!/usr/bin/env python3

inputs, outputs = [], []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input,output = [l.split(' ') for l in line.split(' | ')]
        inputs.append(input)
        outputs.append(output)

# Part 1
print(f'Part 1: {len([value for output in outputs for value in output if (len(value.strip()) > 1 and len(value.strip()) < 5) or (len(value.strip()) == 7)])}')

# Part 2
def check(input, digit):
    return all([i in input for i in digit])

def calc_digits(input):
    digits = ['','','','','','','','','','']
    ## first iteration to determine all unique number of segments (1,4,7,8)
    for digit in input:
        digit = digit.strip()
        if len(digit) == 2:
            digits[1] = digit
        elif len(digit) == 3:
            digits[7] = digit
        elif len(digit) == 4:
            digits[4] = digit
        elif len(digit) == 7:
            digits[8] = digit

    ## second iteration, to determine remaining numbers
    for value in ([i.strip() for i in input if i.strip() not in digits]):
        value = value.strip()
        if len(value) == 6:
            if check(value, digits[7]):
                if check(value, digits[4]):
                    digits[9] = value
                else:
                    digits[0] = value
            else:
                digits[6] = value
        else:
            if check(value, digits[7]):
                digits[3] = value
            else:
                if 1 == len([i in value for i in digits[4] if i not in value]):
                    digits[5] = value
                else:
                    digits[2] = value

    return [''.join(sorted(d)) for d in digits]

def calc_output_value(line, digits):
    value = []
    for output in [''.join(sorted(o)) for o in line]:
        value.append(digits.index(output.strip()))

    return int(''.join(map(str,value)))

count = 0
for i in range(len(inputs)):
    digits = calc_digits(inputs[i])
    count += calc_output_value(outputs[i], digits)

print(f'Part 2: {count}')