def test():

    assert func(4,6,8) == (28, 'hello', 8), "Wrong Answer"
    
    assert(
    "x=a*b" in __solution__ or 'x = a * b' in __solution__ or "x = a*b" in __solution__ or "x= a*b" in __solution__ or "x =a*b" in __solution__
    ), "Wrong answer: Please check x value"

    assert(
    "y=x+a" in __solution__ or "y = x + a" in __solution__ or "y = x+a" in __solution__ or "y= x+a" in __solution__ or "y =x+a" in __solution__
    ), "Wrong answer: Please check y value"

    assert(
    "z='hello'" in __solution__ or 'z="hello"' in __solution__ or "z = 'hello'" in __solution__ or 'z = "hello"' in __solution__ or 'z= "hello"' in __solution__ or 'z ="hello"' in __solution__ or "z= 'hello'" in __solution__ or "z ='hello'" in __solution__ 
    ), "Wrong answer: Please check z value"
    
    assert(
    "func(4,6,8)" in __solution__ 
    ), "Wrong answer: You chose wrong values or there are spaces between function input values. Please recheck the values or please delete the spaces e.g. func(1,2,3) "
    
    __msg__.good("Great Answer")
