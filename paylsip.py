import datetime
import sys
import csv


class Shift():
    BASE_RATE = 27.64

    def __init__(self):
        self.total = 0
        self.name = ""
        self.total_hours_worked = 0
        self.total_tax = 0

    def __str__(self):
        return f"""
    {self.name}
    Total hours worked: {self.total_hours_worked}
    Total Payable: {self.total}
    Total Tax Paid: {self.total_tax}
    """


def get_date():
    date = input("Enter date of shift (YYYY-MM-DD): ")
    return datetime.date.fromisoformat(date)


def main():

    shift = Shift()

    date = get_date()
    shift.name = f"Shift: {date}"

    print(date)
    print(shift)
    ...


if __name__ == "__main__":
    main()
