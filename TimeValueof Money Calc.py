# TimeValueOfMoney by Ahmet Ali Yildiz
import locale


def main():
    print("Welcome to the Time Value of Money Calculator!")
    print()
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/") :
        locale.setlocale(locale.LC_ALL,'en_US')
    choice = getChoice()
    while choice != 0:
        print()
        if choice == 1:
            amtRec = getValue ("Amount to be receieved: ")
            #deposit = getValue("Initial Deposit: ")
            rate = getValue("Annual Interest Rate (6.5%=6.5): ")
            while rate < 1.0 or rate > 25.0:
                print("Rate is out of normal range: 1-25% only allowed.")
                rate = getValue("Annual Interest Rate (6.5%=6.5)")
            term = getTerm()
            PV = calcPV(amtRec,rate,term)
            print("A monthly deposit of %s" % locale.currency(amtRec, grouping=True)
                  + " earning "
                  + "{:.2%}".format(rate / 100) + " annually for " + str(term) + " months "
                  + "will have a final value of:  %s" % locale.currency(PV,grouping=True) )
            print("That includes interest earned of: %s" % locale.currency((amtRec - PV), grouping=True))

        elif choice == 2:
            deposit = getValue("Initial Deposit: ")
            rate = getValue("Annual Interest Rate (6.5%=6.5): ")
            while rate < 1.0 or rate > 25.0:
                print("Rate is out of normal range: 1-25% only allowed.")
                rate = getValue("Annual Interest Rate (6.5%=6.5)")
            term = getTerm()
            FV = calcFV(deposit,rate,term)
            print("A monthly deposit of %s" % locale.currency(deposit, grouping=True)
                  + " earning "
                  + "{:.2%}".format(rate / 100) + " annually for " + str(term) + " months "
                  + "will have a final value of:  %s" % locale.currency(FV,grouping=True) )
            print("That includes interest earned of: %s" % locale.currency((FV - deposit), grouping=True))

        elif choice == 3:
            #perform FV-Annuity operation...
            deposit = getValue("Monthly Deposit: ")
            rate = getValue("Annual Interest Rate (6.5%=6.5): ")
            while rate < 1.0 or rate > 25.0:
                print("Rate is out of normal range: 1-25% only allowed.")
                rate = getValue("Annual Interest Rate (6.5%=6.5)")
            term = getTerm()
            fva = calcFVA(deposit,rate,term)
            #print("Values = " + str(deposit) + ", " + str(rate) + ", " + str(term) + ", FVA: " + str(fva))
            print("A monthly deposit of %s" % locale.currency(deposit,grouping=True)
                  + " earning "
                  + "{:.2%}".format(rate/100) + " annually after " + str(term) + " months "
                  + "will have a final value of:  %s" % locale.currency(fva,grouping=True) )
            print("That includes interest earned of: %s" % locale.currency((fva-(deposit*term)), grouping=True))
        else:
            print("Unknown Financial Operation.")
        choice = getChoice()
    print("Thank you for using the Financial Calculator.")

def calcPV(d,r,t):
    morate = r / 12.0 / 100.0
    PV = d / ((1+morate) ** t)
    return PV

def calcFV(d,r,t):
    morate = r / 12.0 / 100.0
    FV = d * ((1+morate) ** t)
    return FV

def calcFVA(d,r,t):
    morate = r / 12.0 / 100.0
    fv = 0.0
    # the range function includes the left value, but excludes the right value
    for i in range(0,t):
        intearn = (fv + d) * morate
        fv += intearn + d
    return fv

def getChoice():
    #runs until 0,1,2,or 3 is given by the user
    goodVal = False #boolean
    while not goodVal:
        try:
            choice = int(input("Select Operation: 1=PV, 2=FV, 3=FV-Annuity, 0=Quit: "))
            if choice < 0 or choice > 3:
                print("Unknown operation: 1-3 or 0 to quit only.")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: integers between 0 and 3 only.")
    return choice

def getValue(prompt):
    goodVal = False
    while not goodVal:
        try:
            v = float(input(prompt))
            if v <= 0:
                print("Positive values only here, please...")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: numbers > 0 only, please...")
    return v

def getTerm():
    # hw
    t = 0
    while t <= 0:
        try:
            t = int(input("Enter the Term (in months): "))
            if t <= 0:
                print("Term must be positive, Please re-enter.")
        except ValueError:
            print("Illegal input: positive integers only please.")
    return t

if __name__ == "__main__":
    main()
