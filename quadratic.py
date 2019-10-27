from basic import int_input
import matplotlib.pyplot as plt
import numpy as np


class quadratic:
    """
    deal with quadratic formula
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
        calculate quadratic equation and return value list
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
        calculate quadratic equation value
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

    def inequality(self, direction):
        """
        calculate quadratic inequality value
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
            [3] : inequality + quality
                True >= or <=
                False > or <
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
            return solution
        elif direction == 0 or direction == 2:
            solution.append(0)
            solution.append(solutions[0])
            solution.append(solutions[1])
        else:
            solution.append(1)
            solution.append(solutions[0])
            solution.append(solutions[1])
        if direction == 2 or direction == 3:
            solution.append(True)
        else:
            solution.append(False)
        return solution

    def output_inequality_solution(self, direction):
        """
        quadratic inequality value transform to str
        Returns
        -------
        result : str
            print inequality
        """
        solution = self.inequality(direction)
        if solution[0] == 0:
            if solution[3]:
                return "x <= {}, {} <= x".format(solution[1], solution[2])
            else:
                return "x < {}, {} < x".format(solution[1], solution[2])
        elif solution[0] == 1:
            if solution[3]:
                return "{} <= x <= {}".format(solution[1], solution[2])
            else:
                return "{} < x < {}".format(solution[1], solution[2])
        elif solution[0] == 2:
            return "x != 0"
        elif solution[0] == 3:
            return "x ∈ R"
        else:
            return "x = 0"

    def function_graph(self):
        """
        plot quadratic function graph
        """
        x_max = int_input("input x max")
        x_min = int_input("input x min")
        x = np.arange(x_min, x_max, 0.1)
        y = self.a * x ** 2 + self.b * x + self.c
        plt.plot(x, y)
        plt.show()

    def function_variation(self):
        """
        make formula from quadratic formula
        Returns
        -------
        result : str
            a(x-p)+q
        """
        return "{}(x - {})^2 + {}".format(
                                        self.a,
                                        self.b / (self.a * 2),
                                        self.c - self.a * (self.b / self.a / 2) ** 2)


if __name__ == "__main__":
    test = quadratic()
    print(test.function_variation())
