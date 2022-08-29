#AssetDDL by Ahmet Ali Yildiz

class AssetDDL:
    """Double Declining Depreciation"""

    def __init__(self, c=0, s=0, lf=0):
        self._errmsg = ""
        self.setCost(c)
        self.setSalvage(s)
        self.setLife(lf)
        if self.isValid():
            self.buildAssetDDL()

    def setCost(self, v):
        self._cost = v

    def getCost(self):
        return self._cost

    def setSalvage(self, v):
        self._salvage = v

    def getSalvage(self):
        return self._salvage

    def setLife(self, v):
        self._life = v

    def getLife(self):
        return self._life

    def isValid(self):
        valid = True
        if self._cost <= 0:
            self._errmsg = "Cost must be positive"
            valid = False
        elif self._life <= 0:
            self._errmsg = "life must be positive"
            valid = False
        elif self._salvage < 0:
            self._errmsg = " Salvage cannot be less than zero "
            valid = False
        elif self._salvage >= self._cost:
            self._errmsg = "Salvage must be less than cost"
            valid = False
        return valid

    def getErrorMsg(self):
        return self._errmsg

    def buildAssetDDL(self):
        self._bbal = [0] * self._life
        self._ebal = [0] * self._life
        self._anndep = [0] * self._life
        self._deppct = [0] * self._life

        # need Straight Line rate
        self._deprate = (1.0 / self._life) * 2.0
        #SL annDep
        self._depSL = (self._cost - self._salvage) / self._life

        #working dep var
        depwrk = 0


        self._bbal[0] = self._cost
        for i in range(0, self._life):
            if i > 0:
                self._bbal[i] = self._ebal[i - 1]
            depwrk = self._bbal[i] * self._deprate
            if depwrk < self._depSL:
                depwrk = self._depSL
            if (self._bbal[i] - depwrk) < self._salvage:
                depwrk = self._bbal[i] - self._salvage

            self._anndep[i] = depwrk
            self._ebal[i] = self._bbal[i] - self._anndep[i]
            self._deppct[i] = self._anndep[i] / self._cost

    def getAnnDep(self, yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._anndep[yr-1]

    def getBBal(self, yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._bbal[yr - 1]

    def getEBal(self, yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._ebal[yr - 1]
    def getDepPct(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._deppct[yr-1]
