class ComplexNumber:
    real: float = 0.0
    imaginary: float = 0.0
    pass

def create(real, imaginary):
    """Create complex number with given real and imaginary parts."""
    c = ComplexNumber()
    c.real = real
    c.imaginary = imaginary
    return c

def add(c1: ComplexNumber, c2: ComplexNumber):
    """Add two complex numbers."""
    c = ComplexNumber()
    c.real = c1.real + c2.real
    c.imaginary = c1.imaginary + c2.imaginary
    return c

def subtract(c1: ComplexNumber, c2: ComplexNumber):
    """Subtract two complex numbers."""
    c = ComplexNumber()
    c.real = c1.real - c2.real
    c.imaginary = c1.imaginary - c2.imaginary
    return c

def multiply(c1: ComplexNumber, c2: ComplexNumber):
    """Multiply two complex numbers."""
    c = ComplexNumber()
    c.real = c1.real * c2.real - c1.imaginary * c2.imaginary
    c.imaginary = c1.real * c2.imaginary + c1.imaginary * c2.real
    return c

def conjugate(c: ComplexNumber):
    """Return the conjugate of a complex number."""
    c_conj = ComplexNumber()
    c_conj.real = c.real
    c_conj.imaginary = -c.imaginary
    return c_conj