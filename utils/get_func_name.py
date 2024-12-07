import inspect

def getFuncName() -> str:
    """ Return the name of the caller function. """
    # Get the current stack frame
    frame = inspect.currentframe()
    # Go up one level in the stack to get the caller's frame
    caller_frame = frame.f_back
    # Get the caller's code object
    caller_code = caller_frame.f_code
    # Return the caller's function name
    return caller_code.co_name

if __name__ == '__main__':
    print(getFuncName())  # <module>

    def test():
        print(getFuncName())  # test
    
    test()