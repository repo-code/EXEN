def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "import keras" in __solution__, "Wrong answer"
    assert "import tensorflow" in __solution__, "Wrong answer"
    assert "import matplotlib" in __solution__, "Wrong answer"
    assert "import pandas" in __solution__, "Wrong answer"
    assert "import numpy" in __solution__, "Wrong answer"
    assert "import scipy" in __solution__, "Wrong answer"
    assert "import sklearn" in __solution__, "Wrong answer"
    assert "import cv2" in __solution__, "Wrong answer"
    assert x == 10, "Wrong value"
    assert y == 2, "Wrong value"
    assert z == x/y, "Wrong z"
    assert a == z * 2, "Wrong a"
    assert "print(a)" in __solution__, "Wrong print"
    assert "print('Done!')" in __solution__, "Wrong print"

    __msg__.good("Well done!")
