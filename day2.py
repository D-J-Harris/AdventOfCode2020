"""Password Philosophy"""

with open('inputs/day2.txt', 'r') as f:
    inp = []
    for line in f.readlines():
        inps = line.split()
        ranges = list(map(int, inps[0].split('-')))
        target = inps[1][0]
        password = inps[2]
        inp.append((ranges, target, password))

count_1 = 0
count_2 = 0
for trial in inp:
    first, second = trial[0][0], trial[0][1]
    target = trial[1]
    password, pass_len = trial[2], len(trial[2])

    count_1 += first <= password.count(target) <= second
    if first <= pass_len and second <= pass_len:
        count_2 += (password[first-1] == target) is not (password[second-1] == target)

print(f'answer to puzzle 1 is {count_1}')
print(f'answer to puzzle 2 is {count_2}')
