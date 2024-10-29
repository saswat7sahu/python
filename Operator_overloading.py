#operator overloading
#Operator overloading is a feature in some programming languages that allows developers
#  to redefine the behavior of operators (such as +, -, *, etc.) for user-defined data types.
#This is particularly useful in domains like mathematics, physics simulations, and game development, where such operations are frequent and natural to the problem domain.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Operator overloading
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __repr__(self):
        return f"({self.real} + {self.imag}i)"
num1=ComplexNumber(3,5)
num2=ComplexNumber(4,8)
res=num1*num2
print(res)