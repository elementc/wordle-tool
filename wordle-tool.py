#!/usr/bin/python3
import sys
import os

if len(sys.argv) not in [2,3,4]:
    print("Usage: wordle-tool.py dot_pattern [burned_letters] [misplaced_letters]")
    exit(1)

dot_pattern = sys.argv[1]
burned_letters = ""
misplaced_letters = ""
if len(sys.argv) > 2:
    burned_letters = sys.argv[2]
if len(sys.argv) > 3:
    misplaced_letters = sys.argv[3]


if len(dot_pattern) != 5:
    print("dot_pattern must be 5 long to be a wordle")
    exit(2)

print(f"dot_pattern: {dot_pattern}")
print(f"burned_letters: {burned_letters}")
print(f"mistplaced_latters: {misplaced_letters}")

command = f"cat /etc/dictionaries-common/words | grep ^{dot_pattern}\$"
for letter in burned_letters:
    command += f" | grep -v {letter}"
for letter in misplaced_letters:
    command += f" | grep {letter}"
os.system(command)

