import numpy as np
import main

def test_zeros():
    assert np.all(main.zeros(3) == np.zeros(3))