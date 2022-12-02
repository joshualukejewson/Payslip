import datetime
import sys
import csv
import re


class Shift():
# BASE PAY RATE and SATURDAY and SUNDAY rate.
    BASE_RATE = 27.64
    SATURDAY = 1.25
    SUNDAY = 1.50

    def __init__(self):
        self.total_earnt = 0
        self.hours_worked = 0
        self.rate = 0

# Print payslip information
    def __str__(self):
        return f"""
    {self.name}
    Total hours worked: {self.hours_worked} x ${self.rate}
    Total Payable: {self.total_earnt}
    """
# Set the name with the date format
    def set_name(self, name):
        self.name = name

def main():

    shift = Shift()
    date = get_date()
    shift.rate = get_rate(date, shift)
    shift.name = f"Shift: {date}"
    shift.hours_worked = get_hours_worked()
    shift.total_earnt = get_total_earnt(shift)

    write_to_file(shift)

    print(shift)

def write_to_file(shift):
    ...
    
def get_total_earnt(s):
    return (s.rate * s.hours_worked)

def get_rate(d, shift):
    if (0 <= d.month <= 4):
        return shift.BASE_RATE
    elif d.month == 5:
        return shift.BASE_RATE * shift.SATURDAY
    else:
        return shift.BASE_RATE * shift.SUNDAY

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
    return round(hours_diff.total_seconds() /60 / 60, 3)

if __name__ == "__main__":
    main()
