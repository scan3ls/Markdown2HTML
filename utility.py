"""
    Utility Functions
"""


def err_print(*args, **kwargs):
    """
        err_print - prints to stderr

        Arguments:
            args - same as print *args
            kwargs - same as print **kwargs
    """
    from sys import stderr
    print(*args, file=stderr, **kwargs)
