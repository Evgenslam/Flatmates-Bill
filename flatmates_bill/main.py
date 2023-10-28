from flat import Bill, Flatmate
from reports import PDFReport, FileSharer


"""
Version of program using console. Outputs a link for the report of split bills to download from a filesharer.
Another version using Flask and browser interface is also available.
"""

amount = int(input('How much was the bill this month: '))
period = (input('Please enter ther period. E.q. June 2022: '))

name1 = input('Please enter the name of the first flatmate: ')
days_in_house1 = int(input(f'How many days did {name1} stay in the house: '))

name2 = input('Please enter the name of the second flatmate: ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house: '))

mybill = Bill(amount, period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(flatmate1.pays(bill=mybill, flatmate2=flatmate2))
print(flatmate2.pays(bill=mybill, flatmate2=flatmate1))

pdf_report = PDFReport(filename=f'{mybill.period}.pdf')

pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=mybill)

filesharer = FileSharer(pdf_report.filename)
print(filesharer.share())


