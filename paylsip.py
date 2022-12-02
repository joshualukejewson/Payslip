import datetime
import sys
import csv
import re


class Payslip():
# BASE PAY RATE and SATURDAY and SUNDAY rate.
    BASE_RATE = 27.64
    SATURDAY = 1.25
    SUNDAY = 1.50

    def __init__(self):
        self.total_earnt = 0
        self.total_hours_worked = 0
        self.total_tax = 0

# Print payslip information
    def __str__(self):
        return f"""
    {self.name}
    Total hours worked: {self.total_hours_worked}
    Total Payable: {self.total_earnt}
    Total Tax Paid: {self.total_tax} 
    """
# Set the name with the date format
    def set_name(self, name):
        self.name = name

def main():

    payslip = Payslip()
    date = get_date()
    payslip.name = f"Shift: {date}"

    hours_worked = get_hours_worked()
    print(f"{hours_worked} hours")

    print(date)
    print(payslip)

def get_date():
    date = input("Enter date of shift (YYYY-MM-DD): ")
    return datetime.date.fromisoformat(date)

def get_hours_worked():

    start_time = input("When did you start?: ")
    matches_start = re.match(r"(2[0-4]|1[0-9]|[1-9])\:([0-5]?[0-9])", start_time)
    end_time = input("When did you finish?: ")
    matches_end = re.match(r"(2[0-4]|1[0-9]|[1-9])\:([0-5]?[0-9])", end_time)

    start_hour = int(matches_start[1])
    start_minutes = int(matches_start[2])

    end_hour = int(matches_end[1])
    end_minutes = int(matches_end[2])

    start_delta = datetime.timedelta(hours=start_hour, minutes=start_minutes)
    end_delta = datetime.timedelta(hours=end_hour, minutes=end_minutes)

    hours_diff = (end_delta - start_delta)
    return (hours_diff.total_seconds() /60 / 60)

if __name__ == "__main__":
    main()
