def main():
    s = int(input())
    e = int(input())
    d = int(input())

    acc = 0
    for i in range(s, e + 1, d):
        acc += i
        
    print(acc)

if __name__ == '__main__':
    main()
