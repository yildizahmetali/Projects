#Annuity by Ahmet Ali Yildiz

class Annuity:

    def __init__(self,a=0.0,r=0.0,t=0.0):
        # create 'private' variables for the class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildAnnuity()
    #set and get methods 'encapsulate' data values
    def setAmt(self,value):
        self._amt = value
    def getAmt(self):
        return self._amt

    def setRate(self,value):
        self._rate = value
    def getRate(self):
        return self._rate

    def setTerm(self,value):
        self._term = value
    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
        if self._amt <= 0:
            self._error = "Amount must be positive."
            valid = False
        elif self._rate < 1 or self._rate > 25:
            self._error = "Rate out of bounds: 1 to 25 only."
            valid = False
        elif self._term <= 0:
            self._error = "Term must be positive."
            valid = False
        return valid


    def getError(self):
        return self._error

    def buildAnnuity(self):
        build = False
        try:
            self._bbal = [0] * self._term
            self._intearn = [0] * self._term
            self._ebal = [0] * self._term

            self._bbal[0] = 0
            morate = self._rate / 12.0 / 100.0
            for i in range(0, self._term):
                if i > 0:
                    self._bbal[i] = self._ebal[i-1]
                self._intearn[i] = (self._bbal[i] + self._amt) * morate
                self._ebal[i] = self._bbal[i] + self._amt + self._intearn[i]
            build = True
        except Exception as ex:
            self._error = "Annuity build failed: " + ex
            build = False

    def getFVA(self):
        return self._ebal[self._term-1]

    def getBBal(self,mo=0):
        if mo < 1 or mo > self._term:
            self._error = " Invalid month of: " + str(mo) + " requested."
            return -1
        return self._bbal[mo-1]
    def getIntEarn(self,mo=0):
        if mo < 1 or mo > self._term:
            self._error = " Invalid month of: " + str(mo) + " requested."
            return -1
        return self._intearn[mo-1]
    def getEndBal(self,mo):
        if mo < 1 or mo > self._term:
            self._error = " Invalid month of: " + str(mo) + " requested."
            return -1
        return self._ebal[mo-1]
    def getInterest(self):
        return self._ebal[self._term-1] - (self._amt * self._term)
