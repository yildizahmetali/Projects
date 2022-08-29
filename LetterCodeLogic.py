#LetterCodeLogic = the business processes for LetterCode, by Ahmet Ali Yildiz

class LetterCodeLogic:
    """Encode/Decode Message"""

    @staticmethod
    def Decode(msg):
        #issue: string comes as, ex: "1,2,0,3"
        #to decode we must parse string into 1, 2, 0, and 3
        #(decode will use ASCII/Unicode values)

        nums = msg.split(",") #method of strings to split into list based on delimiter
        result = ""
        for x in nums:
            try:
                #strip method not needed for our purposes but will trim leading/trailing spaces
                n = int(x.strip()) #convert list entry x into integer
                if n ==0:
                    c = " " #special case of zero = space in result
                elif n < 1 or n > 36:
                    #n is out of range
                    c = "?"
                else:
                    #n is in range for A-Z
                    c = chr(n+64)
            except ValueError:
                #list entry x was not an integer
                c = "?" #must return ? in final result string

            result += c
        return result

    @staticmethod
    def Encode(msg):
        #allow lower case input but convert to upper case...
        #process (upper case) msg a character by character...
        #for each character the conversion is the logical 'reverse; of decode...
        #must find reverse method of chr()
        #must make sure that values are in range for return or 99 goes back
        #space is still a special case

        letters = list(msg)
        result = ""
        for y in letters:
            #try:
            y = y.upper()
            if y == " ":
                c = "0" #special case of zero = space in result
            else:
                #n is in range for A-Z
                i = ord(y)-64
                if i < 1 or i > 26:
                    c = "99"
                else:
                    i = str(i)
                    c = i
            #except ValueError:
                #list entry x was not an integer
                #c = "?" #must return ? in final result string

            result += " " + c
        return result
