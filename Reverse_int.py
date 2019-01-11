# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new = ''
        for s in reversed(str(abs(x))):
            new = new+s
        if int(new) > 2**(31)-1:
            return 0
        if x < 0:
            return -int(new)
        return int(new)