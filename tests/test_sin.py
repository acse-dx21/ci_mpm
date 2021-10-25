
import numpy as np
from simple_functions import my_sin


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_sin(self):
        '''Test computation of pi'''
        mysin = my_sin(2)
        assert np.isclose(mysin, np.sin(2), atol=1e-12)