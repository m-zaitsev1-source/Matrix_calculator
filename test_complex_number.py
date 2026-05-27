import libraries.complex_number as cn
from libraries.complex_number import *
def test_create_complex_number():
    c1 = create(1.0, 2.0)
    assert c1.real == 1.0
    assert c1.imaginary == 2.0
    c2 = create(3.0, 4.0)
    assert c2.real == 3.0
    assert c2.imaginary == 4.0
    c3 = add(c1, c2)
    assert c3.real == 4.0
    assert c3.imaginary == 6.0
test_create_complex_number()