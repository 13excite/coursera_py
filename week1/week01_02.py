import sys

num_steps = int(sys.argv[1])


n = num_steps - 2
for stairs in range(1, num_steps):
    print(' ' * n, '#' * stairs)
    n -= 1
print('#' * num_steps)

