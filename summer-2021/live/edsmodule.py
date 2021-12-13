bigstring = "these are all the thoughts I ever had, in one string: hmm......"

def gigantify(x):
    """makes an otherwise ordinary number gigantic"""
    if x > 1:
        return (x**x)**x
    else:
        raise ValueError('x should be bigger than 1 to gigantify')

class TestClass:
    def __init__(self, x):
        self.x = x
       
    def print(self):
        print(f'my x value is {x}')
        
        