# Loan by Ahmet Ali Yildiz

class Loan:
    """Loan Calculator"""

    def __init__(self, a=0, r=0, t=0):
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildLoan()

    def setAmt(self, value):
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
        return  self._error

    def buildLoan(self):
        build = False
        try:
            self._bbal = [0] * self._term
            self._intchg = [0] * self._term
            self._ebal = [0] * self._term

            # Loan needs monthly payment
            morate = self._rate / 12.0 / 100.0
            denom = ((1+morate) ** self._term) - 1.0
            self._mopmt = (morate + morate / denom) * self._amt

            self._bbal[0] = self._amt
            for i in range(0,self._term):
                if i > 0:
                    self._bbal[i] = self._ebal[i-1]
                self._intchg[i] = self._bbal[i] * morate
                self._ebal[i] = self._bbal[i] + self._intchg[i] - self._mopmt
            build = True
        except Exception as ex:
            self._error = "Loan build fail: " + ex
            build = False

    def getMoPmt(self):
        return self._mopmt

    def getBegBal(self, mo = 0):
        if mo < 1 or mo > self._term:
            self._error = "No beginning balance for Loan month " + str(mo)
            return -1
        return self._bbal[mo-1]

    def getIntChg(self, mo = 0):
        if mo < 1 or mo > self._term:
            self._error = "No interest charge for loan month " + str(mo)
            return -1
        return self._intchg[mo-1]
    def getEndBal(self, mo = 0):
        if mo < 1 or mo > self._term:
            self._error = "No ending balance for Loan month " + str(mo)
            return -1
        return self._bbal[mo-1]

    def getInterest(self):
        return (self._mopmt * self._term) - self._amt
