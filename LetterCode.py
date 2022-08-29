#LetterCode (user interface program) - by Ahmet Ali Yildiz

#from file import class...

from LetterCodeLogic import LetterCodeLogic

def main():
    print("Welcome to the Letter Code Program")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            #Encode process using LetterCodeLogic Encode method
            msg = input("Enter letters to encode: ")
            r = LetterCodeLogic.Encode(msg)
            print("Your Encoded Message is: \n" + r)
        elif choice == 2:
            #Decode process using LetterCodeLogic Decode method
            msg = input("Enter numbers to decode (separated by commas): ")
            r = LetterCodeLogic.Decode(msg)
            print("Your Decoded Message is: \n" + r)
        else:
            print("I did not understand your choice.")
        choice = getChoice()

    print("Thank you for using the Letter Code Program!")




def getChoice():
    goodVal = False #boolean
    while not goodVal:
        try:
            choice = int(input("Choice? (1=Encode, 2=Decode, 0=Quit):  "))
            if choice < 0 or choice > 2:
                print("Unknown operation: 1-2 or 0 to quit only.")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: integers between 0 and 2 only.")
    return choice





if __name__ == "__main__":
    main()
