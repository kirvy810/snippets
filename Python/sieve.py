def main():
    N = 100 + 1

    sieve = [True] * N
    sieve[0] = sieve[1] = False

    for i in range(2, N):
        if not sieve[i]: continue

        print(i, end=' ')
        
        for j in range(2 * i, N, i):
            sieve[j] = False


if __name__ == '__main__':
    main()
