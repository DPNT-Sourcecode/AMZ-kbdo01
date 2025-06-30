
class SumSolution:

    def compute(self, a:int, b:int) -> int:
    #def sumSolution(a: int, b: int) -> int:
        """
        Sums two positive integers between 0 and 100 (inclusive).

        :param a: First integer (0-100)
        :param b: Second integer (0-100)
        :return: Sum of a and b
        :raises ValueError: If a or b is not between 0 and 100
        """
        if not (0 <= a <= 100) or not (0 <= b <= 100):
            raise ValueError("Both numbers must be between 0 and 100 inclusive.")
        return a + b


    #def compute(self, x, y):
    #    raise NotImplementedError()
