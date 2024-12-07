import inspect

def getClassName() -> str:
    """ Return the name of the caller class.
     
    Currently only works with an instance method.
    """
    # Get the current stack frame
    frame = inspect.currentframe()
    # Go up one level in the stack to get the caller's frame (which is the method's frame)
    caller_frame = frame.f_back
    # Get the caller's class object
    caller_class = caller_frame.f_locals.get('self', None)
    if caller_class is not None:
        return caller_class.__class__.__name__
    else:
        raise RuntimeError('Cannot determine caller class name. Make sure this method is called within a class method.')

if __name__ == '__main__':
    class MyClass:
        def test(self):
            print(getClassName())  # MyClass

    test = MyClass()
    test.test()