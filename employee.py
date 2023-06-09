import datetime
import random

INFLATION = 0.027
DATE_FORMAT = "%m/%d/%Y"
UUID_LENGTH = 25
SEP = "|"


class Employee:
    def __init__(
        self,
        rate: float = None,
        first: str = None,
        middle: str = None,
        last: str = None,
        start_date: datetime.datetime = None,
        end_date: datetime.datetime = None,
        birth_date: datetime.datetime = None,
    ) -> None:
        uuid_length = UUID_LENGTH
        self.uuid = int(
            "".join([str(random.randint(0, 1)) for i in range(uuid_length)])
        )
        self.rate = rate
        self.first = first
        self.middle = middle
        self.last = last
        self.start_date = start_date
        self.end_date = end_date
        self.birth_date = birth_date

    def __repr__(self) -> str:
        return f"""
        | Employee : {self.uuid}
        | Full Name: {self.first} {self.middle} {self.last}
        | Start Date: {self.returnDate(self.start_date)}
        | End Date: {self.returnDate(self.end_date)}
        | Birth Date: {self.returnDate(self.birth_date)}
        | Hourly Rate: ${self.rate}
        | OT Rate: ${self.rate*1.5}
        """

    def asDict(self):
        return {
            "Employee": self.uuid,
            "First": self.first,
            "Middle": self.middle,
            "Last": self.last,
            "Start": self.returnDate(self.start_date),
            "End": self.returnDate(self.end_date),
            "Hourly": self.rate,
        }

    def returnDate(self, date: datetime.datetime) -> str:
        return (
            datetime.datetime.strftime(date, DATE_FORMAT) if date is not None else "N/A"
        )

    def calculatePay(self, hours_worked: int | float) -> float:
        return (
            self.rate * hours_worked
            if hours_worked <= 40
            else (self.rate * hours_worked) + (self.rate * 0.5) * (hours_worked - 40)
        )

    def promote(self, rate_increase: int | float):
        self.rate += rate_increase
        print(f"{self.first} got promoted!")

    def terminate(self):
        if self.end_date is not None:
            print(
                f"{self.first} was already terminated on {self.returnDate(self.end_date)}"
            )
        else:
            self.end_date = datetime.datetime.now()
            print(f"{self.first} just got terminated..")


# for testing:
if __name__ == "__main__":
    tanner = Employee(
        rate=18.00,
        first="Twanker",
        middle="The",
        last="Confused",
        start_date=datetime.datetime(month=1, day=25, year=2022),
        birth_date=datetime.datetime(month=3, day=28, year=1989),
    )

    joey = Employee(
        rate=25.00,
        first="Joey",
        middle="The-Blade",
        last="F",
        start_date=datetime.datetime(month=2, day=15, year=2016),
        birth_date=datetime.datetime(month=6, day=18, year=1991),
    )

    employees = [joey, tanner]
    print(employees)

    joey.promote(0.5)

    print(f"{joey.first} will get paid ${joey.calculatePay(45)}")

    print(f"{tanner.first} will get paid ${tanner.calculatePay(32)}")

    for employee in employees:
        promotion_amount = employee.rate * INFLATION
        employee.promote(promotion_amount)

    tanner.terminate()
    joey.promote(2)
    print(employees)
    tanner.terminate()
    tanner_dict = tanner.asDict()
    joey_dict = joey.asDict()
    employee_dict = {k: [v] for k, v in tanner_dict.items()}
    [employee_dict[k].append(v) for k, v in joey_dict.items()]
    for k, v in employee_dict.items():
        k = k.ljust(10)
        v1 = str(v[0]).ljust(UUID_LENGTH)
        v2 = str(v[1]).ljust(UUID_LENGTH)
        print(k, v1, v2, sep=SEP)
