import math
import OneVariableApproximations
import unittest

class NewtonMethodTest(unittest.TestCase):
    def test_willFindRootOfSimpleFunction(self):
        func = lambda x: x
        derivative = lambda x: 1

        try:
            result = OneVariableApproximations.findRootWithNewtonMethod(func, derivative, -5, 20, 0.001)
            self.assertEquals(result.root, 0)
            print(result.allApproximations)
        except OneVariableApproximations.NoApproximationFound as fail:
            print(fail.approximations)
            self.fail()

    def test_willNotFindRootOfFunctionWithNoRoot(self):
        func = lambda x: x**2 + 1
        derivative = lambda x: 2*x

        with (self.assertRaises(OneVariableApproximations.NoApproximationFound)):
            OneVariableApproximations.findRootWithNewtonMethod(func, derivative, 5, 20, 0.001)

    def test_willFindRootOfComplexFunction(self):
        func = lambda x: math.cos(x) - x
        derivative = lambda x: -1 * math.sin(x) - 1

        result = OneVariableApproximations.findRootWithNewtonMethod(func, derivative, math.pi / 4, 20, 0.001)
        error = abs(0 - result.rootFunctionValue)
        self.assertLessEqual(error, 0.001)
