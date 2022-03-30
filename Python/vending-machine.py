COINS = (500, 100, 50, 10, 5, 1)
MENU = [
    ('콜라', 1000),
    ('사이다', 1500),
    ('물', 700),
    ('커피', 2300),
]


def main():
    while True:
        print('===== [ MENU ] =====')
        print('( 0 ) 나가기')
        for i, (name, price) in enumerate(MENU, 1):
            print(f'( {i} ) {name} : {price}원')
        print('====================\n')

        while True:
            n = int(input('선택 > '))

            if n == 0:
                print('** 종료 **')
                return
            elif 1 <= n <= len(MENU):
                n -= 1
                break
            else:
                print('잘못된 선택입니다.')

        money = int(input('돈을 넣으세요 > '))
        while money < MENU[n][1]:
            money += int(input('(잔액 부족!) 돈을 더 넣으세요 > '))

        money -= MENU[n][1]

        print(f'\n** {MENU[n][0]} 나왔어요! **\n')

        if money == 0:
            continue

        print('== [ CHANGE ] ==')
        for coin in COINS:
            count, money = divmod(money, coin)
            if count != 0:
                print(f'{coin:>3}원 : {count}개')
        print('================\n')


if __name__ == '__main__':
    main()
