def main():
    N = 100

    sieve = [True] * (N + 1)

    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if not sieve[i]:
            continue

        for j in range(2 * i, N + 1, i):
            sieve[j] = False

    for n, is_prime in enumerate(sieve):
        if is_prime:
            print(n, end=' ')


if __name__ == '__main__':
    main()
