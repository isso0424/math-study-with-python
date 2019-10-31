import math
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
