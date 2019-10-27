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
        solution : list(float)
            solution value of quadratic equation
        """
        D = self.b ** 2 - 4 * self.a * self.c
        solution = []
        if D > 0:
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)) / 2 * self.a)
            solution.append((-self.b - pow(self.b**2 - 4 * self.a * self.c, 0.5)) / 2 * self.a)
        elif D == 0:
            solution.append(-self.b / (2 * self.a))
        else:
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)))
            solution.append((-self.b + pow(self.b**2 - 4 * self.a * self.c, 0.5)))
        return solution

    def inequality(self, direction):
        """
        Parameters
        ----------
        direction : int
            if it is 0, inequality is >
            if it is 1, inequality is <
            if it is 2, inequality is >=
            if it is 3, inequality is <=
        Returns
        -------
        solution : list(complex), None
            [0] : x < solutions[0], solutions[1] < x => 0
                or
                solutions[0] < x solutions[1] => 1
                or
                x != 0 => 2
                or
                x is all real numbers => 3
                or
                x = 0 => 4
            [1] : solutions[0]
            [2] : solutions[1]
            if no solution, return None
        """
        solution = []
        solutions = self.equation_value()
        solutions.sort()
        print(solutions)
        if len(solutions) == 1:
            if direction == 0:
                solution.append(2)
                solution.append(0)
            elif direction == 1:
                return None
            elif direction == 2:
                solution.append(3)
            else:
                solution.append(4)
                solution.append(0)
        elif direction == 0 or direction == 2:
            solution.append(0)
            solution.append(solutions[0])
            solution.append(solutions[1])
        else:
            solution.append(1)
            solution.append(solutions[0])
            solution.append(solutions[1])
        return solution


if __name__ == "__main__":
    test = quadratic()
    print(test.equation_value())
    print(test.inequality(2))
