INPUT_HOUR_MSG = "Enter your hours: "
INPUT_RATE_MSG = "Enter your hourly rate: "
MSG = "Pay: $"


def computeWeeklyPay(hours: int | float | str, rate: int | float | str) -> float:
    """
    calclulates and returns the weekly pay for an individual after accounting for any applicaple overtime.
    """
    hours, rate = float(hours), float(rate)

    pay = hours * rate
    if hours > 40:
        pay += (hours - 40) * (rate * 0.5)
    return pay


if __name__ == "__main__":
    hours_worked = input(INPUT_HOUR_MSG)
    hourly_rate = input(INPUT_RATE_MSG)
    pay = computeWeeklyPay(hours_worked, hourly_rate)
    print(f"{MSG}{pay}")
