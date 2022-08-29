#Foreign Currency Calculator by Ahmet Ali Yildiz

import locale

#globals for exchange rates
rEUR = rGBP = rJPY = rCAD = rRUB = 0

def getRates():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    print("Please enter the currency rates per US $")
    rEUR = getOneRate("EUR: ")
    rGBP = getOneRate("GBP: ")
    rJPY = getOneRate("JPY: ")
    rCAD = getOneRate("CAD: ")
    rRUB = getOneRate("RUB: ")

def getOneRate(prompt):
    r = float(input(prompt))
    return r

def doValuation():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    #print("Rates were: " + str(rEUR) + " " + str(rGBP) + " " + str(rJPY) + " " + str(rCAD) + " " + str(rRUB) )
    grandtot = 0.0
    #lists to hold units and total purchases for each currency
    cnames = ["EUR","GBP","JPY","CAD","RUB"]
    totunits = [0,0,0,0,0]
    totcval = [0.0,0.0,0.0,0.0,0.0]

    choice = getChoice()
    while choice != 0:
        cval = 0.0
        qty = 0
        if choice == 1:
            #Euros
            qty = getAmount("Euros")
            cval = qty * rEUR
            print(str(qty) + " Euros has a value of: %s " %locale.currency(cval,grouping=True))
            totunits[0] = totunits[0] + qty
            totcval[0] = totcval[0] + cval
            #Pounds
        elif choice == 2:
            qty = getAmount("Pounds Sterling")
            cval = qty * rGBP
            print(str(qty) + " Pounds has a value of: %s " %locale.currency(cval,grouping=True))
            totunits[1] += qty
            totcval[1] += cval
            #Yen
        elif choice == 3:
            qty = getAmount("Yen")
            cval = qty * rJPY
            print(str(qty) + " Yen has a value of: %s " %locale.currency(cval,grouping=True))
            totunits[2] += qty
            totcval[2] += cval
            #CAD
        elif choice == 4:
            qty = getAmount("CAD")
            cval = qty * rCAD
            print(str(qty) + " CAD has a value of: %s " %locale.currency(cval,grouping=True))
            totunits[3] += qty
            totcval[3] += cval
            #Ruble
        elif choice == 5:
            qty = getAmount("Ruble")
            cval = qty * rRUB
            print(str(qty) + " Ruble has a value of: %s " %locale.currency(cval,grouping=True))
            totunits[4] += qty
            totcval[4] += cval

        elif choice == 9:
            print("Please enter the currency rates per US $")
            rEUR = getOneRate("EUR: ")
            rGBP = getOneRate("GBP: ")
            rJPY = getOneRate("JPY: ")
            rCAD = getOneRate("CAD: ")
            rRUB = getOneRate("RUB: ")

        else:
            print("Currency option unknown or not implemented.")

        grandtot += cval

        choice = getChoice()
    print("Totals: ")
    for i in range(0,5):
        print(cnames[i] + ": " + str(totunits[i]) + " units for a valuse of %s " %locale.currency(totcval[i],grouping=True) )

    print("The grand total of all purchases was: %s " %locale.currency(grandtot,grouping=True))



def getAmount(prompt):
    q = int(input("How many " +prompt + " are you buying? "))
    return q

def getChoice():
    choice = -1
    while choice < 0 or (choice > 5 and choice != 9):
        try:
            choice = int(input("Currency? 1=EUR,2=GBP,3=JPY,4=CAD,5=RUB,9=New Rates, 0=quit: "))
            if choice <0 or choice > 5 and choice !=9:
                print("Unknown choice: 1-5, 9 or 0 only.")
        except ValueError:
            print("Illegal input: integers from 0-5 or 9 only.")
    return choice

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')

    print("Welcome to the Foreign Currency Calculator.")

    getRates()
    doValuation()

    print("Thanks for using the currency calculator")

if __name__ == "__main__":
    main()
