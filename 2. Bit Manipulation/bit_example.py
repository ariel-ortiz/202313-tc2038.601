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


def is_power_of_2(n: int) -> bool:
    return (n & (n - 1)) == 0


def twos_complement(n: int) -> int:
    return (~n) + 1


def binary(n: int) -> str:
    if n == 0:
        return '0'
    result: list[str] = []
    while n:
        result.append(str(n & 1))
        # if (n & 1) == 1:
        #     result.append('1')
        # else:
        #     result.append('0')
        n >>= 1
        # n = n >> 1
    return ''.join(result[::-1])


print(f'{is_even(5) = }')
print(f'{is_even(2135132513453452) = }')
print(f'{is_power_of_2(4) = }')
print(f'{is_power_of_2(512) = }')
print(f'{is_power_of_2(4096) = }')
print(f'{is_power_of_2(666) = }')
print(f'{is_power_of_2(1000) = }')
print(f'{is_power_of_2(3) = }')
print(f'{twos_complement(5) = }')
print(f'{twos_complement(-42) = }')
print(f'{binary(5) = }')
print(f'{binary(10) = }')
print(f'{binary(0) = }')
print(f'{binary(42) = }')
print(f'{binary(1024) = }')
print(f'{binary(1023) = }')

# Value swaping

# Using a temporary var
x = 5
y = 8
print(f'\n{x = }, {y = }')
t = x
x = y
y = t
print(f'{x = }, {y = }')

# Using parallel assignment (destructuring)
x = 5
y = 8
print(f'\n{x = }, {y = }')
x, y = y, x
print(f'{x = }, {y = }')

# XOR value swapping
x = 5
y = 8
print(f'\n{x = }, {y = }')
x = x ^ y
y = x ^ y
x = x ^ y
print(f'{x = }, {y = }')
