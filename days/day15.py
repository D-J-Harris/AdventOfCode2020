"""Rambunctious Recitation"""
from itertools import islice


def complete(first):
    inp = [19, 20, 14, 0, 9, 1]
    length = len(inp)
    spoken = []
    spoken_indices = {}
    rng = 2020 if first else 30000000
    for i in range(rng):
        num = inp[i % length]
        if i in range(length):
            spoken.append(num)
            spoken_indices[num] = [i]
        else:
            last_spoken = spoken[-1]
            if len(spoken_indices[last_spoken]) == 1:
                spoken.append(0)
                if 0 in spoken_indices:
                    spoken_indices[0].append(i)
                else:
                    spoken_indices[0] = [i]
            else:
                speak = spoken_indices[last_spoken][-1]-spoken_indices[last_spoken][-2]
                spoken.append(speak)
                if speak in spoken_indices:
                    spoken_indices[speak].append(i)
                else:
                    spoken_indices[speak] = [i]
    return spoken[-1]


print(f"answer to puzzle 1 is {complete(first=True)}")
print(f"answer to puzzle 2 is {complete(first=False)}")
