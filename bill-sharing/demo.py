from classes import Bill, Renter, PdfReport

if __name__ == "__main__":

    print("Welcome to our bill sharing demo app!!!")
    period_hint = "(e.g. March 2021 or December 2019)"
    period = input(f"Which month is this bill for {period_hint}?? >")
    amt_hint = "(e.g. 500, 64.79)"
    amount = float(input(f"What amount was due for {period} {amt_hint}?? >$"))
    this_bill = Bill(amount = amount, time_period = period)

    print("\nBill information received!")
    n_renters = None
    while n_renters is None:
        user_n = int(input(f"How many people are paying this {this_bill}?? >"))
        if user_n <= 0:
            print("Please enter a whole number greater than zero... ")
        else:
            n_renters = user_n

    renter_list = []
    for i in range(n_renters):
        renter_days = None
        print(f"Info for renter {i + 1} of {n_renters}")
        renter_name = input("Name: ")
        while renter_days is None:
            days_prompt = f"For how many days is {renter_name} paying?? >"
            user_days = int(input(days_prompt))
            if user_days <= 0:
                print("Please enter a whole number greater than zero... ")
            else:
                renter_days = user_days
        this_renter = Renter(name = renter_name, days_in_apt = renter_days)
        renter_list.append(this_renter)
        print("---------------------\n")


    print("Ready to generate bill sharing breakdown!")
    pdf_maker = PdfReport(bill = this_bill, renters = renter_list)
    auto_open_choice = None
    while auto_open_choice is None:
        user_choice = input("Open PDF report automatically?? (y/n) >")
        if user_choice.lower() not in ['y', 'n']:
            print("Please choose 'y' or 'n'... ")
        else:
            auto_open_choice = True if user_choice == 'y' else False
    pdf_maker.generate(auto_open = auto_open_choice)








