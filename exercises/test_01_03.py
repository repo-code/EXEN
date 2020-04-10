def test():

    assert func(4,6,8) == (28, 'hello', 8), "...أجابة خاطئة يرجى اعادة التحقق من الجواب"
    
    assert(
    "x=a*b" in __solution__ or 'x = a * b' in __solution__ or "x = a*b" in __solution__ or "x= a*b" in __solution__ or "x =a*b" in __solution__
    ), "أجابة خاطئة تأكد من قيمة x"

    assert(
    "y=x+a" in __solution__ or "y = x + a" in __solution__ or "y = x+a" in __solution__ or "y= x+a" in __solution__ or "y =x+a" in __solution__
    ), "أجابة خاطئة تأكد من قيمة y"

    assert(
    "z='hello'" in __solution__ or 'z="hello"' in __solution__ or "z = 'hello'" in __solution__ or 'z = "hello"' in __solution__ or 'z= "hello"' in __solution__ or 'z ="hello"' in __solution__ or "z= 'hello'" in __solution__ or "z ='hello'" in __solution__ 
    ), "أجابة خاطئة تأكد من قيمة z"
    
    assert(
    "func(4,6,8)" in __solution__ 
    ), "Wrong answer: You chose wrong values or there are spaces between function input values. Please recheck the values or please delete the spaces e.g. func(1,2,3) "
    
    __msg__.good("اجابة صحيحة ، احسنت")
