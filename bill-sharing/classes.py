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


    def split(self):
        '''if bill splitting works how I think it does, it makes more sense 
        to take an array of renters'''
        pass


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


    def get_name(self):
        bill_period = self.bill.time_period.replace(" ","-")
        return f"SharedBill_{bill_period}.pdf"


    def generate(self):
        pass




if __name__ == "__main__":

    test_bill = Bill(amount = 420.69, time_period = "February 2022")
    dude_one = Renter(name = "Colonel Sanders", days_in_apt = 21)
    dude_two = Renter(name = "Seymour Skinner", days_in_apt = 14)

    print(test_bill)
    print(dude_one)
    print(dude_two)









