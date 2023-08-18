x = 5
y = 8
z = 10

# AND
print(f'{x & y = :08b}')
print(f'{y & z = :08b}')

# OR
print(f'{x | y = :08b}')
print(f'{y | z = :08b}')

# XOR
print(f'{x ^ y = :08b}')
print(f'{y ^ z = :08b}')

# NOT
print(f'{~x = }')
print(f'{~~y = }')

# SHL
print(f'{x << 1 = }')
print(f'{y << 3 = }')

# SHR
print(f'{x >> 1 = }')
print(f'{y >> 3 = }')


def is_even(n: int) -> bool:
    return (n & 1) == 0


print(f'{is_even(5) = }')
print(f'{is_even(2135132513453452) = }')
