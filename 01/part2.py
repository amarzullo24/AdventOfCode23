import re

CANDIDATES = [str(i) for i in range(1,10)] + ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
answer = 0

str2int = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

with open('input.txt', 'r') as fin:
    for line in fin:
        line = line.strip()
        digits = re.findall(r"(?=("+'|'.join(CANDIDATES)+r"))", line)
        digits = [digit if not digit in str2int else str2int[digit] for digit in digits]
        digit = int(f"{digits[0]}{digits[-1]}")
        answer += digit

print("The answer is:", answer)
        