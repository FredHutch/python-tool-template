def foo():
    """
    example function documentation
    an example doctest is included below    
    returns: None
    
    >>> x = foo()
    >>> x
    'foo'

    """
    return "foo"


#this is a handy shorthand that specifies:
#IF you run this module directly, executute the following.
# This is often used for code the defines functions used elsewhere (ie: it's a package)
# That will run some stand-alone test or script if called directly (ie: python foo.py)
if __name__ == "__main__":
    import doctest
    doctest.testmod()