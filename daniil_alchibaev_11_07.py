class Complex:
    def __init__(self, real: float, imag: float = 0.):
        self.real, self.imag = real, imag

    def __add__(self, other):
        result = Complex(self.real + other.real, self.imag + other.imag)
        return result

    def __str__(self):
        sign = '+' if self.imag > 0 else '-'
        return f'{self.real} {sign} {abs(self.imag)}j'

    def __mul__(self, other):
        result_real = self.real * other.real - self.imag * other.imag
        result_imag = self.real * other.imag + self.imag * other.real
        return Complex(result_real, result_imag)


if __name__ == '__main__':
    complex_num1 = Complex(2, 3)
    complex_num2 = Complex(3, -1)
    print(complex_num1, complex_num2, complex_num1 + complex_num2, complex_num1 * complex_num2)
