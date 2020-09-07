class NoApproximationFound(Exception): 
    def __init__(self, approximations):
        self.approximations = approximations

class RootResult:
    def __init__(self, initials):
        self.allApproximations=initials
        self.root = None
        self.rootFunctionValue = None

def findRootWithNewtonMethod(function, derivative, initial, maxIterations, tolerance):
    previousApproximation = initial
    
    result = RootResult([initial])
    for i in range(maxIterations):
        nextApproximation = (previousApproximation - 
            function(previousApproximation) / derivative(previousApproximation))
        
        result.allApproximations.append(nextApproximation)

        if (abs(function(nextApproximation) - 0) <= tolerance):
            result.root = nextApproximation
            result.rootFunctionValue = function(nextApproximation)
            return result
        
        previousApproximation = nextApproximation
    
    raise NoApproximationFound(result.allApproximations)

def findRootWithSecantMethod(function, initial, secondInitial, maxIterations, tolerance):
    previous = secondInitial
    grandPrevious = initial

    result = RootResult([grandPrevious, previous])
    for i in range(maxIterations):
        nextApproximation = previous - function(previous) * (previous - grandPrevious) / \
            (function(previous) - function(grandPrevious))

        result.allApproximations.append(nextApproximation)

        if (abs(nextApproximation - previous) < tolerance):
            result.root = nextApproximation
            result.rootFunctionValue = function(nextApproximation)
            return result
        
        grandPrevious = previous
        previous = nextApproximation

    raise NoApproximationFound(result.allApproximations)

        


