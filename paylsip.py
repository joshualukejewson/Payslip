import datetime
import sys
import csv


class Shift():
    BASE_RATE = 27.64

    def __init__(self, date):
        self.total = 0
        self.name = date
        self.total_hours_worked = 0
        self.total_tax = 0

    def __str__(self):
        return f"""
    {self.name}
    Total hours worked: {self.total_hours_worked}
    Total Payable: {self.total}
    Total Tax Paid: {self.total_tax}
    """


def main():

    date = input("Enter date of shift (YYYY-MM-DD): ")
    date = datetime.date.fromisoformat(date)
    shift = Shift(date)

    print(date)
    print(shift)
    ...


if __name__ == "__main__":
    main()
