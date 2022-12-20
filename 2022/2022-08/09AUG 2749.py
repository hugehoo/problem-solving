a, b = 0, 1
mod_ = 1_000_000
for _ in range(int(input()) % (15 * (10**5))):
    a, b = b % mod_, (a + b) % mod_

print(a)
