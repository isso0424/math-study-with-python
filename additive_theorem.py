from math import sin, cos
import basic


class Add_theorem:
    # this class process add theorem processing
    def add_sin(self, x, y):
        """
        this function process {sin(x + y)}
        Parameters
        ----------
        x : float
        y : float
            these parameters are parameter of sin
        Returns
        -------
        sin_x_y : float
            this value is sin(x+y)
        """

    def add_cos(self, x, y):
        """
        this function process cos(x+y)
        Parameters
        ----------
        x : float
        y : float
            these parameters are parameter of cos
        Returns
        -------
        cos_x_y : float
            this value is cos(x+y)
        """

    @staticmethod
    def product_sum_formula(x, y, mode):
        """
        this function calculate sin or cos sum from product
        Parameters
        ----------
        x : float
        y : float
            these are sin or cos parameters
        mode : int
            change formula
            0 : sin(x)cos(y) = {sin(x+y)+sin(x-y)}/2
            1 : cos(x)sin(y) = {sin(x+y)+sin(y-x)}/2
            2 : sin(x)sin(y) = {cos(x+y)+cos(x-y)}/2
            3 : cos(x)cos(y) = {cos(y-x)-cos(x+y)}/2
        Returns
        -------
        result : float
            this value is product sum formula value
        """
        if mode == 0:
            result = (sin(x + y) + sin(x - y)) / 2
        elif mode == 1:
            result = (sin(x + y) + sin(y - x)) / 2
        elif mode == 2:
            result = (cos(x + y) + cos(x - y)) / 2
        elif mode == 3:
            result = (cos(y - x) + cos(x + y)) / 2
        else:
            raise ValueError("mode is between 0 and 3")
        return result

    @staticmethod
    def sum_product_formula(x, y, mode):
        """
        this function calculate sin or cos sum from product
        Parameters
        ----------
        x : float
        y : float
            these are sin or cos parameters
        mode : int
            change formula
            0 : sin(x) + sin(y) = 2sin{(x+y)/2}cos{(x-y)/2}
            1 : sin(x) - sin(y) = 2cos{(x+y)/2}sin{(x-y)/2}
            2 : cos(x) + cos(y) = 2cos{(x+y)/2}cos{(x-y)/2}
            3 : cos(y) - cos(x) = 2sin{(x+y)/2}sin{(x-y)/2}
        Returns
        -------
        result : float
            this value is product sum formula value
        """
        if mode == 0:
            result = 2 * (sin((x+y)/2)*cos((x-y)/2))
        elif mode == 1:
            result = 2 * (cos((x+y)/2)*sin((x-y)/2))
        elif mode == 2:
            result = 2 * (cos((x+y)/2)*cos((x-y)/2))
        elif mode == 3:
            result = 2 * (sin((x+y)/2)*sin((x-y)/2))
        else:
            raise ValueError("mode is between 0 and 3")
        return result
