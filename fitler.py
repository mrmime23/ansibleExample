#!/usr/bin/python

class thing(object):
    def ABC(self):
        return {
            'X': self.XYZ
        }

    def XYZ(self, UY):
        WER = UY + ' LOL'
        return WER

class thing2(object):
    def __init__(self):
        self.something = []

    def PQR(self, Z):
        self.something.append(Z)

    def DFG(self):
        NML = ""
        for JK in self.something:
            NML += str(JK) + " GHI "
        return NML

if __name__ == "__main__":
    A_instance = thing()
    B = A_instance.ABC()
    C = B['X']('123')
    print(C)

    Q_instance = thing2()
    Q_instance.PQR(100)
    Q_instance.PQR(200)
    RST = Q_instance.DFG()
    print(RST)
