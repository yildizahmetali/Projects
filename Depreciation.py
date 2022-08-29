# Depreciation.py by Ahmet Ali Yildiz

import locale
import os
from Asset import Asset
from AssetDDL import AssetDDL

cost = 0
salv = 0
life = 0

def doDepreciation():
    global cost, salv, life

    asset = Asset(cost,salv,life)
    addl = AssetDDL(cost,salv,life)
    if asset.getErrorMsg() == "" and addl.getErrorMsg() == "":
        print("Straight Line Depreciation per year = %s " %locale.currency(asset.getAnnDep(), grouping=True))
        print("First year Double Declining depreciation = %s " %locale.currency(addl.getAnnDep(1), grouping=True))
        sched = input("Schedule: <S>L, <D>DL, <B>oth, <N>one (S,D,B,N): ")
        if len(sched) > 0 and (sched[0].upper() == "S" or sched[0].upper() == "B") :
            # do straight line schedule
            print("\n       Straight Line Schedule")
            print("Year     Beg.Bal.    Ann.Dep.    End.Bal.")
            for i in range(1,asset.getLife()+1):
                print("{:4}".format(i) +
                      "{:13,.2f} {:13,.2f} {:13,.2f}".format(asset.getBBal(i), asset.getAnnDep(),asset.getEBal(i)))

        if len(sched) > 0 and (sched[0].upper() == "D" or sched[0].upper() == "B"):
            print("\n       Double Declining Schedule")
            print("Year     Beg.Bal.    Ann.Dep.    End.Bal     Dep.Pct.")
            for i in range(1,addl.getLife()+1):
                print("{:4}".format(i) +
                      "{:13,.2f} {:13,.2f} {:13,.2f} {:13.2%}".format(addl.getBBal(i), addl.getAnnDep(i),addl.getEBal(i),addl.getDepPct(i)))
    else:
        print("Asset error: " + asset.getErrorMsg() + " / " + addl.getErrorMsg())

def getValue(prompt,dtype):
    goodVal = False
    while not goodVal:
        try:
            if dtype.lower() == "i":
                val = int(input(prompt))
            elif dtype.lower() == "f":
                val = float(input(prompt))
            else:
                val = 0
            goodVal = True
        except ValueError as ex:
            print("Illegal data input for type: " + dtype + " " + str(ex))
            goodVal = False
    return val

def getAssetFile():
    global cost, salv, life
    print("Asset Files Available")

    filenames = []
    cwd = os.getcwd()   # get current working directory
    fnum = 0
    for entry in os.listdir(cwd):
        path = os.path.join(cwd,entry)      #creates a full, absolute path to the file
        if os.path.isfile(path) and entry.endswith(".ast"):
            fnum += 1
            print(str(fnum) + ": " + entry)
            filenames.append(path)
    if fnum == 0:
        print("Sorry, no asset files found.")
        cost = 0
        salv = 0
        life = 0
        path = None
    if fnum > 1:
        path = ""
    else:
        path = filenames[0]
    try:
        while path == "":
            fnum = int(input("\nWhich Asset File (enter #): "))
            if fnum < 1 or fnum > len(filenames):
                print("File Number chosen is out of range.")
            else:
                path = filenames[fnum-1]
        fl = open(path,'r')
        cost = float(fl.readline())
        salv = float(fl.readline())
        life = int(fl.readline())
        fl.close()
    except OSError as ex:
        print("Asset file " + path + " could not be processed: " + str(ex))
        cost = 0
        salv = 0
        life = 0
        path = None
    except ValueError as ex:
        print("File number not numeric or asset file damaged")
        cost = 0
        salv = 0
        life = 0
        path = None
    return path



def main():
    global cost, salv, life
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL,'en_US')

    choice = input("Asset by: <i>nput, <f>ile, or <q>uit: (i,f,q): ").upper()
    while len(choice) > 0 and choice[0] != "Q":
        if choice[0] == "I":
            cost = getValue("Asset Cost: ","f")
            salv = getValue("Salvage Value: ","f")
            life = getValue("Life (years): ","i")
        else:
            path = getAssetFile()
            #path returns as 'None' if no file selected or process failed in some way
            if path != None:
                print("File " + path + " read with values: " +str(cost) + ", " + str(salv) + ", " + str(life))
        if cost > 0:
            doDepreciation()
        else:
            print("Asset not processed")

        choice = input("Asset by: <i>input, <f>file, or <q>quit: (i,f,q): ").upper()
        print()

    print("Thank you for using the Depreciation Calculator")


if __name__ == "__main__":
    main()
# Depreciation.py by Ahmet Ali Yildiz

import locale
import os
from Asset import Asset
from AssetDDL import AssetDDL

cost = 0
salv = 0
life = 0

def doDepreciation():
    global cost, salv, life

    asset = Asset(cost,salv,life)
    addl = AssetDDL(cost,salv,life)
    if asset.getErrorMsg() == "" and addl.getErrorMsg() == "":
        print("Straight Line Depreciation per year = %s " %locale.currency(asset.getAnnDep(), grouping=True))
        print("First year Double Declining depreciation = %s " %locale.currency(addl.getAnnDep(1), grouping=True))
        sched = input("Schedule: <S>L, <D>DL, <B>oth, <N>one (S,D,B,N): ")
        if len(sched) > 0 and (sched[0].upper() == "S" or sched[0].upper() == "B") :
            # do straight line schedule
            print("\n       Straight Line Schedule")
            print("Year     Beg.Bal.    Ann.Dep.    End.Bal.")
            for i in range(1,asset.getLife()+1):
                print("{:4}".format(i) +
                      "{:13,.2f} {:13,.2f} {:13,.2f}".format(asset.getBBal(i), asset.getAnnDep(),asset.getEBal(i)))

        if len(sched) > 0 and (sched[0].upper() == "D" or sched[0].upper() == "B"):
            print("\n       Double Declining Schedule")
            print("Year     Beg.Bal.    Ann.Dep.    End.Bal     Dep.Pct.")
            for i in range(1,addl.getLife()+1):
                print("{:4}".format(i) +
                      "{:13,.2f} {:13,.2f} {:13,.2f} {:13.2%}".format(addl.getBBal(i), addl.getAnnDep(i),addl.getEBal(i),addl.getDepPct(i)))
    else:
        print("Asset error: " + asset.getErrorMsg() + " / " + addl.getErrorMsg())

def getValue(prompt,dtype):
    goodVal = False
    while not goodVal:
        try:
            if dtype.lower() == "i":
                val = int(input(prompt))
            elif dtype.lower() == "f":
                val = float(input(prompt))
            else:
                val = 0
            goodVal = True
        except ValueError as ex:
            print("Illegal data input for type: " + dtype + " " + str(ex))
            goodVal = False
    return val

def getAssetFile():
    global cost, salv, life
    print("Asset Files Available")

    filenames = []
    cwd = os.getcwd()   # get current working directory
    fnum = 0
    for entry in os.listdir(cwd):
        path = os.path.join(cwd,entry)      #creates a full, absolute path to the file
        if os.path.isfile(path) and entry.endswith(".ast"):
            fnum += 1
            print(str(fnum) + ": " + entry)
            filenames.append(path)
    if fnum == 0:
        print("Sorry, no asset files found.")
        cost = 0
        salv = 0
        life = 0
        path = None
    if fnum > 1:
        path = ""
    else:
        path = filenames[0]
    try:
        while path == "":
            fnum = int(input("\nWhich Asset File (enter #): "))
            if fnum < 1 or fnum > len(filenames):
                print("File Number chosen is out of range.")
            else:
                path = filenames[fnum-1]
        fl = open(path,'r')
        cost = float(fl.readline())
        salv = float(fl.readline())
        life = int(fl.readline())
        fl.close()
    except OSError as ex:
        print("Asset file " + path + " could not be processed: " + str(ex))
        cost = 0
        salv = 0
        life = 0
        path = None
    except ValueError as ex:
        print("File number not numeric or asset file damaged")
        cost = 0
        salv = 0
        life = 0
        path = None
    return path



def main():
    global cost, salv, life
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL,'en_US')

    choice = input("Asset by: <i>nput, <f>ile, or <q>uit: (i,f,q): ").upper()
    while len(choice) > 0 and choice[0] != "Q":
        if choice[0] == "I":
            cost = getValue("Asset Cost: ","f")
            salv = getValue("Salvage Value: ","f")
            life = getValue("Life (years): ","i")
        else:
            path = getAssetFile()
            #path returns as 'None' if no file selected or process failed in some way
            if path != None:
                print("File " + path + " read with values: " +str(cost) + ", " + str(salv) + ", " + str(life))
        if cost > 0:
            doDepreciation()
        else:
            print("Asset not processed")

        choice = input("Asset by: <i>input, <f>file, or <q>quit: (i,f,q): ").upper()
        print()

    print("Thank you for using the Depreciation Calculator")


if __name__ == "__main__":
    main()
