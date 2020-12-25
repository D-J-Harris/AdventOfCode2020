"""Combo Breaker"""

c_pk = 15113849
d_pk = 4206373

divider = 20201227
subject_num = 7


def pk_to_encryption(pk, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= pk
        val = val % divider
    return val


c_loop, d_loop = None, None
loop_counter, val = 0, 1
while not c_loop or not d_loop:
    loop_counter += 1
    val *= subject_num
    val = val % divider
    if val == c_pk:
        c_loop = loop_counter
    if val == d_pk:
        d_loop = loop_counter

print(f'answer to puzzle is {pk_to_encryption(c_pk, d_loop)}')
