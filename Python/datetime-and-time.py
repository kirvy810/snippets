import datetime
import time


def diff_days(s, e):
    return (e - s).days


def get_month(tm):
    return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
           ][tm.tm_mon - 1]


def get_day(tm):
    return '월화수목금토일'[tm.tm_wday]


def us_date_format(tm):
    return '{}-{}-{}'.format(tm.tm_mday, get_month(tm), tm.tm_year)


def main():
    now = time.localtime()
    current_date = datetime.date(now.tm_year, now.tm_mon, now.tm_mday)

    y, m, d = map(int, input('YYYY/MM/DD > ').split('/'))
    date = datetime.date(y, m, d)

    print('오늘은 {}입니다.'.format(us_date_format(now)))

    diff = diff_days(current_date, date)

    if diff < 0:
        print('{}부터 {}일이 지났습니다'.format(date, -diff))
    elif diff > 0:
        print('{}까지 {}일이 남았습니다'.format(date, diff))
    else:
        print('{}은 오늘입니다'.format(date))
        

if __name__ == '__main__':
    main()
