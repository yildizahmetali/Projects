# Conversions.py by Ahmet Ali Yildiz

from Converter import Converter



def main():
    print("Welcome to the English-Metric Converter!")

    doK = False
    ans = input("On Temp Conversions show degrees Kelvin? (Y/N): ")
    if len(ans) > 0 and ans[0].upper() == "Y":
        doK = True

    choice = getChoice()
    while choice != 0:
        # Bubble up exception handling: Converter will throw errors back here...
        try:
            if choice == 1:
                # Mi to KM
                mi = input("Enter Your miles: ")
                ki = Converter.MitoKi(mi)
                print(str(mi) + " Miles = " + str(round(ki, 3)) + " Kilometers.")

            elif choice == 2:
                # Oz to Gr
                oz = input("Enter Your Ounces: ")
                gr = Converter.OztoGr(oz)
                print(str(oz) + " Ounces = " + str(round(gr, 3)) + " Grams.")

            elif choice == 3:
                # F to C
                f = input("Enter Your Fahrenheits: ")
                c = Converter.FtoC(f)
                print(str(f) + " Fahrenheits = " + str(round(c, 3)) + " Celsius.")
                if doK:
                    k = Converter.degreesK(c)
                    print("  Which is also a temp of " + str(round(k,3)) + " Kelvin.")


            elif choice == 4:
                # C to F
                c = input("Enter Your Celsius: ")
                f = Converter.CtoF(c)
                print(str(c) + " Celsius = " + str(round(f, 3)) + " Fahrenheits.")
                if doK:
                    k = Converter.degreesK(c)
                    print("  Which is also a temp of " + str(round(k,3)) + " Kelvin.")

            elif choice == 5:
                # M to ft
                m = input("Enter Your Meters: ")
                ft = Converter.MtoFt(m)
                print(str(m) + " Meters = " + str(round(ft, 3)) + " Feets.")

            elif choice == 6:
                # Li to Gal
                li = input("Enter Your Liters: ")
                gal = Converter.LitoGal(li)
                print(str(li) + " Liters = " + str(round(gal, 3)) + " Gallons.")

            else:
                print("Conversion " + str(choice) + " not yet implemented")
        except ValueError as e:
            print("Data error: " + str(e))
        except Exception as e:
            print("General error: " + str(e))

        choice = getChoice()

    print("Thank you for using the converter.")



def getChoice():
    goodVal = False  # boolean
    while not goodVal:
        try:
            choice = int(
                input("Conversion? (1=Mi-to-Km, 2=Oz-to-Gr, 3=F-to-C, 4=C-to-F, 5=M-to-Ft, 6=Li-to-Gal, 0=end):  "))
            if choice < 0 or choice > 6:
                print("Unknown operation: 1-6 or 0 to quit only.")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: integers between 0 and 6 only.")
    return choice


if __name__ == "__main__":
    main()
