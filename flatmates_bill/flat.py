class Bill:
    """
    Object that contains data about a bill, such as amount and period.
    """

    def __init__(self, amount, period):
        self.amount = int(amount)
        self.period = period


class Flatmate:
    """
    Creates a flatmate who has a name and has to pay a proportional
    share for the bill depending on how many days he or she spends in
    the flat.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = int(days_in_house)

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (flatmate2.days_in_house + self.days_in_house)
        to_pay = round(bill.amount * weight, 2)
        return to_pay