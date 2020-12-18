"""Operation Order"""


def act_op(left, right, op):
    if op == '+':
        return left + right
    if op == '*':
        return left * right


def evaluate(inp, first):
    if first:
        ans = 0
        operator = ''
        for x in inp:
            if isinstance(x, int):
                if ans == 0:
                    ans = x
                else:
                    ans = act_op(ans, x, operator)
            else:
                operator = x
    else:
        for idx, x in enumerate(inp):
            if x == '+':
                tmp = int(inp[idx - 1]) + int(inp[idx + 1])
                del inp[idx - 1]
                inp[idx] = tmp
        ans = 1
        for num in inp:
            if num != '+' and num != '*':
                ans *= num
    return ans


def get_result(line, first):
    subs_count = 0
    subs = [[]]
    for c in line:
        if c == '(':
            subs_count += 1
            subs.append([])
        elif c == ')':
            a = evaluate(subs[-1], first)
            del subs[-1]
            subs_count -= 1
            subs[-1].append(a)
        else:
            if c == ' ':
                continue
            elif c.isnumeric():
                c = int(c)
            subs[subs_count].append(c)
    return evaluate(subs[0], first)


with open('../inputs/day18.txt', 'r') as f:
    ans1, ans2 = 0, 0
    for line in f.read().splitlines():
        ans1 += get_result(line, first=True)
        ans2 += get_result(line, first=False)


print(f'answer to puzzle 1 is {ans1}')
print(f'answer to puzzle 2 is {ans2}')
