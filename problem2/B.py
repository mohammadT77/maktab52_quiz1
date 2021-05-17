import argparse
from datetime import date, timedelta


class WeekdayIterator:

    def __init__(self, start_date: date, end_date: date, week_day: int):
        self.start_date = start_date
        self.end_date = end_date
        self.week_day = week_day

    def __iter__(self):
        for i in range(7):
            first_date = self.start_date + timedelta(days=i)  # First matched week day...
            if first_date.weekday() == self.week_day:
                self.__date = first_date
                return self

    def __next__(self) -> date:
        if self.__date > self.end_date:
            raise StopIteration()
        res = self.__date
        self.__date += timedelta(days=7)
        return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--start-date', metavar='DATE', type=date.fromisoformat, required=True, dest='start_date',
                        help='enter start date')
    parser.add_argument('-e', '--end-date', metavar='DATE', type=date.fromisoformat, default=date.today(),
                        dest='end_date',
                        help='enter end date (default: today)')
    parser.add_argument('-w', '--weekday', metavar='WDAY', type=int, required=True, dest='week_day',
                        help='enter week day')

    args = parser.parse_args()
    weekday_iter = WeekdayIterator(args.start_date, args.end_date, args.week_day)
    for i in weekday_iter:
        print(i)
