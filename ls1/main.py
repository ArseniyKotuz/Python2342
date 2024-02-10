from math import floor, log10

class IntervalError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def arabic_to_roman(number):
    if not number: 
        return ""
    
    romans = {
        0: ["I", "IV", "V", "IX"],
        1: ["X", "XL", "L", "XC"],
        2: ["C", "CD", "D", "CM"],
        3: ["M"]
    }

    decimal = floor(log10(number))
    first = number // 10 ** decimal
    other = number % 10 ** decimal
    if first < 4:
        return f"{romans[decimal][0]*first}{arabic_to_roman(other)}"
    elif first == 4:
        return f"{romans[decimal][1]}{arabic_to_roman(other)}"
    elif first == 5:
        return f"{romans[decimal][2]}{arabic_to_roman(other)}"
    elif first < 9:
        return f"{romans[decimal][2]}{romans[decimal][0]*(first-5)}{arabic_to_roman(other)}"
    elif first == 9:
        return f"{romans[decimal][3]}{arabic_to_roman(other)}"


if __name__ == "__main__":
    while True:
        number = input(f"{'-'*20}\nFor exit use q\nEnter number: ")
        if number == "q":
            break

        try:
            number = int(number)
            if number < 0 or number > 4000:
                raise IntervalError()
            result = arabic_to_roman(number)
            print(result)

        except ValueError:
            print("\n\nError: Invalid Data: Value isn't a number\n\n")
        except IntervalError:
            print("\n\nError: Value not in 0-1000 Interval\n\n")
