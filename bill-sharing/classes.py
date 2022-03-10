import pathlib
import webbrowser

from fpdf import FPDF
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
        self.img_path = "files/house.png"


    def filename(self):
        bill_period = self.bill.time_period.replace(" ","-")
        return f"SharedBill_{bill_period}.pdf"


    def write_report_header(self, pdf_obj:FPDF, img_size:int = 80, 
        heading_size:int = 24, subheading_size:int = 20,
        fontfam:str = "Helvetica"):
        pdf_obj.image(self.img_path, w = img_size, h = img_size)
        pdf_obj.set_font(family = fontfam, size = heading_size, style = "B")
        pdf_obj.cell(w = 0, h = 60, txt = self.heading, border = "B", 
            align = "C", ln = 1)
        pdf_obj.set_font(family = fontfam, size = subheading_size, style = "B")
        pdf_obj.cell(w = 0, h = 40, txt = f"Period: {self.bill.time_period}",
         border = "B", ln = 2)


    def write_payment_details(self, pdf_obj:FPDF, fontsize:int = 16, 
        fontfam:str = "Helvetica"):
        pdf_obj.set_font(family = fontfam, size = fontsize)
        payment_summary = self.bill.split(renters = self.renter_list)
        for renter_name, amount_owed in payment_summary.items():
            line_text = f"{renter_name}: ${amount_owed:,.2f}"
            pdf_obj.cell(w = 0, h = 30, txt = line_text, border = 0, ln = 1)


    def generate(self, auto_open = False):
        pdf = FPDF(orientation = "P", unit = "pt", format = "A4")
        pdf.add_page()
        self.write_report_header(pdf_obj = pdf)
        pdf.ln(h = 40)
        self.write_payment_details(pdf_obj = pdf)
        pdf.output(self.filename())
        if auto_open:
            abs_path = pathlib.Path(self.filename()).resolve()
            browser_path = f"file://{str(abs_path)}"
            print(f"Opening {browser_path}")
            webbrowser.open(browser_path)




if __name__ == "__main__":

    pass









