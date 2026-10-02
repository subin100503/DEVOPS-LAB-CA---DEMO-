"""
Tiny demo app — a couple of simple functions with obvious room for a
CI pipeline to check (tests, linting). Kept small on purpose so the
project stays a "small repo" and the focus stays on the DevOps/CI
pipeline, not on the app itself.
"""


def add(a, b):
    return a + b


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("Is 17 prime?", is_prime(17))
    print("First 10 Fibonacci numbers:", fibonacci(10))

    def multiply(a, b):
    return a * b
