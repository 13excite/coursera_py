import sys

digit_str = sys.argv[1]

sum_numbers = 0
for num in digit_str:
    sum_numbers += int(num)

print(sum_numbers)