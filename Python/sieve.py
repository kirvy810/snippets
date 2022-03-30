def main():
    N = 100

    sieve = [True] * (N + 1)

    sieve[0] = sieve[1] = False

    for i in range(2, N + 1):
        if not sieve[i]:
            continue

        print(i, end=' ')
        for j in range(2 * i, N + 1, i):
            sieve[j] = False


if __name__ == '__main__':
    main()
