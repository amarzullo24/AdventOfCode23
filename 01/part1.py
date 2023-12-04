import re

answer = 0
with open('input.txt', 'r') as fin:
    for line in fin:
        digits = re.findall(r'\d', line.strip())
        digit = int(f"{digits[0]}{digits[-1]}")
        answer += digit

print("The answer is:", answer)
        