# Financials by Ahmet Ali Yildiz

import locale
from Annuity import Annuity
from Loan import Loan


def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Select Operation: 1-Annuity, 2-Loan, 0-Quit: "))
            if choice < 0 or choice > 2:
                print("Unknown operation: 1, 2, or 0 only.")
            else:
                goodVal = True

        except ValueError:
            print("Illegal input: integers 0-2 only.")
            goodVal = False
    return choice


def getValue(prompt, vType):
    # vType is "i if integer is wanted; 'f' if float us wanted
    goodVal = False
    while not goodVal:
        try:
            if vType.lower() == "i":
                amt = int(input(prompt))
            else:
                amt = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return amt


def doAnnuity():
    amt = getValue("Monthly Deposit: ", "f")
    rate = getValue("Annual Interest Rate (6.5%=6.5): ", "f")
    term = getValue("Term (in Months): ", "i")

    ann = Annuity(amt, rate, term)  # instantiation...
    if ann.isValid():
        print("A monthly deposit of %s" % locale.currency(ann.getAmt(), grouping=True)
              + " earning " + "{:.2%}".format(ann.getRate() / 100) + " annually after "
              + str(ann.getTerm()) + " months will have a final value of %s "
              %locale.currency(ann.getFVA(), grouping=True) )
        print("That includes interest earned of: %s " %locale.currency(ann.getInterest(),grouping=True))
        sched = input("Full Schedule? (Y/N): ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Beg.Bal     Deposit     Int.Earned      End.Bal.")
            for i in range(1, ann.getTerm()+1):
                print("{:4}".format(i)
                      + "{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(ann.getBBal(i), ann.getAmt(), ann.getIntEarn(i), ann.getEndBal(i)))
    else:
        print("Annuity error: " + ann.getError())


def doLoan():
    loanamt = getValue("Loan Amount: ", "d")
    rate = getValue("Annual Interest Rate (6.5%=6.5): ", "d")
    term = getValue("Term (in Months): ", "i")
    ln = Loan(loanamt,rate,term)
    if ln.isValid():
        print("A loan of %s" % locale.currency(ln.getAmt(), grouping=True)
              + " costing " + "{:.2%}".format(ln.getRate() / 100) + " annually paid back over "
              + str(ln.getTerm()) + " months will have a monthly payment of %s "
              % locale.currency(ln.getMoPmt(), grouping=True))
        print("That includes total interest charge of: %s " % locale.currency(ln.getInterest(), grouping=True))
        sched = input("Full Schedule? (Y/N): ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Beg.Bal     Payment     Int.Charged      End.Bal.")
            for i in range(1, ln.getTerm() + 1):
                print("{:4}".format(i)
                      + "{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(ln.getBegBal(i), ln.getMoPmt(),
                                                                         ln.getIntChg(i), ln.getEndBal(i)))
    else:
        print("Loan error: " + ln.getError())



def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the financials Calculator")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            doAnnuity()
        elif choice == 2:
            doLoan()
        else:
            print("Operation unknown or not implemented")

        choice = getChoice()
        print()
    print("Thanks for using the Calculator")


if __name__ == "__main__":
    main()
