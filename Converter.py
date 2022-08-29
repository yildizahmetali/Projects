# Converter by Ahmet Ali Yildiz

class Converter:
    """Conversion Algortihms"""

    @staticmethod
    def MitoKi(mi):
        if not isinstance(mi, (int, float)):
            try:
                mi = float(mi)
            except ValueError:
                raise Exception("Illegal miles value: not a numeric")
        if mi <= 0:
            # error: not a legal value for conversion
            raise ValueError("Miles must be a positive value.")
            # return -1
        ki = mi * 1.60934
        return ki

    @staticmethod
    def OztoGr(oz):
        if not isinstance(oz, (int, float)):
            try:
                oz = float(oz)
            except ValueError:
                raise Exception("Illegal ounces value: not a numeric")
        if oz <= 0:
            raise ValueError("Ounces must be a positive value.")

        gr = oz * 28.3495
        return gr

    @staticmethod
    def FtoC(f):
        if not isinstance(f, (int, float)):
            try:
                f = float(f)
            except ValueError:
                raise Exception("Illegal fahrenheit value: not a numeric")

        c = (5/9)*(f - 32)
        return c

    @staticmethod
    def degreesK(c):
        if not isinstance(c,(int,float)):
            c = float(c)
        k = c + 273.15
        if k < 0:
            raise ValueError("Temp is not possible as it is absolute zero.")
        return k


    @staticmethod
    def CtoF(c):
        if not isinstance(c, (int, float)):
            try:
                c = float(c)
            except ValueError:
                raise Exception("Illegal celsius value: not a numeric")

        f = ((9/5)*c) + 32
        return f

    @staticmethod
    def MtoFt(m):
        if not isinstance(m, (int, float)):
            try:
                m = float(m)
            except ValueError:
                raise Exception("Illegal meters value: not a numeric")
        if m <= 0:
            raise ValueError("Meters must be positive value.")

        ft = m * 3.2808
        return ft

    @staticmethod
    def LitoGal(li):
        if not isinstance(li, (int, float)):
            try:
                li = float(li)
            except ValueError:
                raise Exception("Illegal liters value: not a numeric")
        if li <= 0:
            raise ValueError("Liters must be positive value.")

        gal = li * 0.26417
        return gal



