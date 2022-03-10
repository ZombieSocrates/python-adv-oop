from fpdf import FPDF
from pprint import pprint
from typing import List


class Bill:
    '''
    Object that contains data about a bill for a given time period. Requires
    a non-negative amount and a time period expected to be input in month name 
    four-digit year format (%B %Y)
    '''

    def __init__(self, amount:float, time_period:str):
        self.amount = amount
        self.time_period = time_period


    def __str__(self):
        return f"Bill for ${self.amount:,.2f} owed in {self.time_period}"


    def __repr__(self):
        return f"Bill(amount={self.amount}, time_period={self.time_period})"


    def split(self, renters: List["Renter"]) -> dict:
        '''Takes in a list of renters and splits the bill amount across those 
        renters based on how many days they pay for. Returns a dict with
        each renter's name as keys and amount owed as values'''
        total_days = sum([p.days for p in renters])
        split_info = {}
        for renter in renters:
            bill_proportion = renter.days / total_days * self.amount
            split_info[renter.name] = bill_proportion
        return split_info


class Renter:
    '''Object with the name of a person responsible for paying a bill and the 
    total number of days during a billing period they are paying for.
    '''

    def __init__(self, name:str, days_in_apt:int):
        self.name = name
        self.days = days_in_apt

    def __str__(self):
        return f"The homey {self.name} was in da house for {self.days} days"


class PdfReport:
    '''
    Generates a summary report of how a given bill is split across renters in
    PDF format, including the renters' names, the bill period, and how much 
    each renter owes.
    '''
    def __init__(self, bill: "Bill", renters: List["Renter"]):
        self.bill = bill 
        self.renter_list = renters
        self.heading = "Shared Bill Breakdown"


    def filename(self):
        bill_period = self.bill.time_period.replace(" ","-")
        return f"SharedBill_{bill_period}.pdf"


    def generate(self):
        pdf = FPDF(orientation = "P", unit = "pt", format = "A4")
        pdf.add_page()
        pdf.set_font(family = "Helvetica", size = 24, style = "B")
        pdf.cell(w = 100, h = 80, txt = self.heading, border = 1, 
            align = "C", ln = 1)
        pdf.cell(w = 50, h = 40, txt = f"Period: {self.bill.time_period}",
         border = 1)
        pdf.output(self.filename())




if __name__ == "__main__":

    test_bill = Bill(amount = 420.69, time_period = "February 2022")
    dude_one = Renter(name = "Colonel Sanders", days_in_apt = 21)
    dude_two = Renter(name = "Seymour Skinner", days_in_apt = 14)

    print(test_bill)
    print(dude_one)
    print(dude_two)

    split_bill = test_bill.split(renters = [dude_one, dude_two])
    print("Here's the split bill")
    pprint(split_bill)

    pdf_report = PdfReport(bill = test_bill, renters = [dude_one, dude_two])

    print("generating test PDF ...")
    pdf_report.generate()









