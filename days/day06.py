"""Custom Customs"""

with open('../inputs/day06.txt', 'r') as f:
    count_1 = 0
    count_2 = 0
    for block in f.read().split('\n\n'):
        unique_answers = set()
        shared_answers = set(block.split()[0])
        for line in block.split():
            person_answers = set([c for c in line])
            unique_answers.update(person_answers)
            shared_answers = shared_answers.intersection(person_answers)
        count_1 += len(unique_answers)
        count_2 += len(shared_answers)

print(f'answer to puzzle 1 is {count_1}')
print(f'answer to puzzle 2 is {count_2}')
