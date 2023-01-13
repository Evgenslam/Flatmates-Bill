class Bill:
    """
    Object that contains data about a bill, such as amount and period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate who has a name and has to pay a proportional
    share for the bill depending on how many days he or she spends in
    the flat.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (flatmate2.days_in_house + self.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PDFReport:
    """
    Creates a pdf file that contains flatmates' names, bill amount and
    due payment for each flatmate
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(*flatmates, bill):
        pass

bill = Bill(amount=130, period='March 2023')
john = Flatmate(name='John', days_in_house=11)
anton = Flatmate(name='Anton', days_in_house=20)

print(john.pays(bill=bill, flatmate2=anton))
print(anton.pays(bill=bill, flatmate2=john))




