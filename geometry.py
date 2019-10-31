import basic


class Plane:
    # geometry on plane
    def __init__(self):
        x1 = basic.int_input("input x1")
        y1 = basic.int_input("input y1")
        self.coordinate1 = coordinate(x1, y1)
        print(self.coordinate1)

    def internal_dividing_point(self, ratio_x, ratio_y):
        """
        Parameters
        ----------
        ratio_x : float
            self.x1:self.x2 = ratio_x:1
        ratio_y : float
            self.y1:self.y2 = ratio_y:1

        Returns
        -------
        answer :tuple(int, int)
            this tuple have coordinate internal dividing point on (x1, y1)
        """
        pass


class coordinate:
    # date class of coordinate
    def __init__(self, x, y):
        """
        Parameters
        ----------
        x : float
        y : float
         create coordinate (x, y) to use two parameters
        """
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)


if __name__ == "__main__":
    a = Plane()
