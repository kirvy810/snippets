from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
   

def main():
    n = int(input())

    if is_prime(n):
        print(f'{n} is prime')
    else:
        print(f'{n} is not prime')


if __name__ == '__main__':
    main()
