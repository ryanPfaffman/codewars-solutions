import math

'''
Details
Solutions
Forks (4)
Discourse (106)
Collect|
Task
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. 
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman 
symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
| Symbol | Value |
|----------------|
| I      |  1    |
| V      |  5    |
| X      |  10   |
| L      |  50   |
| C      |  100  |
| D      |  500  |
| M      |  1000 |
'''

class RomanNumerals:
    def to_roman(self, n):
        def last_ten(n):
            rtnS = ""

            if n == 9:
                rtnS = "IX"
            elif n == 8:
                rtnS = "VIII"
            elif n == 7:
                rtnS = "VII"
            elif n == 6:
                rtnS = "VI"
            elif n == 5:
                rtnS = "V"
            elif n == 4:
                rtnS = "IV"
            elif n == 3:
                rtnS = "III"
            elif n == 2:
                rtnS = "II"
            elif n == 1:
                rtnS = "I"

            return rtnS


        print(n)
        rtnS = ""

        thousands = int(math.floor(n / 1000))

        rtnS += thousands * "M"

        next = n - (thousands * 1000)
        print("next1\n" + str(next))

        if next > 500:
            if next >= 900:
                rtnS += "CM"
                next -= 900
            else:
                rtnS += "D"
                next -= 500
            hundreds = int(math.floor(next / 100))
            rtnS += hundreds * "C"
        else:
            hundreds = int(math.floor(next / 100))
            rtnS += hundreds * "C"

        next -= hundreds * 100
        print("next2\n" + str(next))

        if next > 50:
            if next >= 90:
                rtnS += "XC"
                next -= 90
            else:
                rtnS += "L"
                next -= 50

            tens = int(math.floor(next) / 10)
            rtnS += tens * "X"

            next -= tens * 10
            rtnS += last_ten(next)
        else:
            if next >= 40:
                rtnS += "XL"
                next -= 40
                rtnS += last_ten(next)
            else:
                tens = int(math.floor(next / 10))
                rtnS += tens * "X"
                next -= tens * 10
                rtnS += last_ten(next)

        return rtnS

    def from_roman(self, s):
        n = 0

        print(s)

        lenS = len(s)
        c = 0
        i = 0


        for x in range(lenS):
            if s[x] == "M":
                if c > 0:
                    if s[x - 1] == "C":
                        n += 900
                    else:
                        n += 1000
                else:
                    n += 1000
            elif s[x] == "D":
                if c > 0:
                    if s[x - 1] == "C":
                        n += 400
                    else:
                        n += 500
                else:
                    n += 500
            elif s[x] == "C":
                if i < (lenS - 1):
                    if s[x + 1] == "D" or s[x + 1] == "M":
                        pass
                    else:
                        if c > 0:
                            if s[x - 1] == "X":
                                n += 90
                            else:
                                n += 100
                        else:
                            n += 100
                else:
                    if c > 0:
                        if s[x - 1] == "X":
                            n += 90
                        else:
                            n += 100
                    else:
                        n += 100
            elif s[x] == "L":
                if c > 0:
                    if s[x - 1] == "X":
                        n += 40
                    else:
                        n += 50
                else:
                    n += 50
            elif s[x] == "X":
                if i < (lenS - 1):
                    if s[x + 1] == "C" or s[x + 1] == "L":
                        pass
                    else:
                        if c > 0:
                            if s[x - 1] == "I":
                                n += 9
                            else:
                                n += 10
                        else:
                            n += 10
                else:
                    if c > 0:
                        if s[x - 1] == "I":
                            n += 9
                        else:
                            n += 10
                    else:
                        n += 10
            elif s[x] == "V":
                if c > 0:
                    if s[x - 1] == "I":
                        n += 4
                    else:
                        n += 5
                else:
                    n += 5
            elif s[x] == "I":
                if i < (lenS - 1):
                    if s[x + 1] == "X" or s[x + 1] == "V":
                        pass
                    else:
                        n += 1
                else:
                    n += 1

            c += 1
            i += 1
        return n
