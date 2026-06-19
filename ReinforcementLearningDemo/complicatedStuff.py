class TrigonometricFunctions:
    def __init__(self):
        pass

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def power(self, base, exp):
        result = 1
        for _ in range(exp):
            result *= base
        return result

    def sin(self, x, num_terms=10):
        x = x % (2 * 3.141592653589793)  # Convert x to the range (-2π, 2π)

        result = 0
        sign = 1

        for n in range(1, num_terms * 2, 2):
            term = (self.power(x, n) / self.factorial(n)) * sign
            result += term
            sign *= -1

        return result

    def cos(self, x, num_terms=10):
        x = x % (2 * 3.141592653589793)  # Convert x to the range (-2π, 2π)

        result = 0
        sign = 1

        for n in range(0, num_terms * 2, 2):
            term = (self.power(x, n) / self.factorial(n)) * sign
            result += term
            sign *= -1

        return result

    def tan(self, x, num_terms=10):
        sin_x = self.sin(x, num_terms)
        cos_x = self.cos(x, num_terms)

        if cos_x == 0:
            raise ValueError("tan(x) is undefined when cos(x) is 0.")

        return sin_x / cos_x

    def arcsin(self, x, num_terms=10):
        if abs(x) > 1:
            raise ValueError("arcsin(x) is only defined for -1 <= x <= 1.")

        result = 0
        sign = 1

        for n in range(1, num_terms * 2, 2):
            term = (self.factorial(2 * n) * self.power(x, 2 * n + 1)) / (
                    2 * n * self.factorial(n) ** 2 * (2 * n + 1)
            ) * sign
            result += term
            sign *= -1

        return result

    def arccos(self, x, num_terms=10):
        return 3.141592653589793 / 2 - self.arcsin(x, num_terms)

    def arctan(self, x, num_terms=10):
        if abs(x) > 1:
            raise ValueError("arctan(x) is only defined for -1 <= x <= 1.")

        result = 0

        for n in range(0, num_terms):
            term = (self.power(x, 2 * n + 1)) / (2 * n + 1)
            result += term * (-1) ** n

        return result

    def ln(self, x, num_terms=10):
        if x <= 0:
            raise ValueError("ln(x) is only defined for x > 0.")

        result = 0

        for n in range(1, num_terms + 1):
            term = (self.power(x - 1, n) / n) * (-1) ** (n + 1)
            result += term

        return result

# Test the TrigonometricFunctions class
trig_functions = TrigonometricFunctions()

angle = 1.5  # In radians
print(f"sin({angle}) ≈ {trig_functions.sin(angle)}")
print(f"cos({angle}) ≈ {trig_functions.cos(angle)}")
print(f"tan({angle}) ≈ {trig_functions.tan(angle)}")

x = 0.5
print(f"arcsin({x}) ≈ {trig_functions.arcsin(x)}")
print(f"arccos({x}) ≈ {trig_functions.arccos(x)}")
print(f"arctan({x}) ≈ {trig_functions.arctan(x)}")

x = 2
print(f"ln({x}) ≈ {trig_functions.ln(x)}")
