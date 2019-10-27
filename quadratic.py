# TODO:はよ書け!!!
from basic import int_input
import math


class quadratic:
    """
    Parameter
    ---------
    self.a : int
        it is a of ax^2 + bx + c
    self.b : int
        it is b of ax^2 + bx + c
    self.c : int
        it is c of ax^2 + bx + c
    """
    def __init__(self):
        formula = "ax^2 + bx + c"
        self.a = int_input("please input a of {}".format(formula))
        self.b = int_input("please input b of {}".format(formula))
        self.c = int_input("please input c of {}".format(formula))

    def equation(self):
        """
        Return
        ------
        solution : list
            solution of quadratic equation
            [0] : -b
            [1] : b^2 ^4ac
            [2] : 2a
            => ([0] +- [1]) / [2] is true solution
        """
        solution = [-self.b,
                    self.b**2 - 4 * self.a * self.c,
                    self.a * 2]
        return solution

    def equation_value(self):
        """
        Return
        ------
        solution : list(complex)
            solution value of quadratic equation
        """
        D = self.b ** 2 - 4 * self.a * self.c
        solution = []
        if D > 0:
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)) / 2 * self.a)
            solution.append((-self.b - pow(self.b**2 - 4 * self.a * self.c, 0.5)) / 2 * self.a)
        elif D == 0:
            solution.append(-self.b / (2 * self.a) + 0j)
        else:
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)))
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)))
        return solution


if __name__ == "__main__":
    test = quadratic()
    print(test.equation_value())
