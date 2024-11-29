import basic

def test_add():
    """ testing add function"""
    assert basic.add(4, 3) == 7, "Error should be 7"
    assert basic.add(4, 3, 2) == 9, "error should be 9"
    return None

def test_mul():
    """ testing mul function"""
    assert basic.mul(4, 3) == 13, "Error should be 13"
    assert basic.mul(4, 3, 2) == 24, "error should be 24"
    return None


def test_div():
    assert basic.div(4, 3) == 1.334, "Error should be 1.334"


def main():
    print("Starting Unit Test...")
    test_add()
    test_mul()
    test_div()
    print("Unit Test Successful")
    return None

if __name__ == "__main__":
    main()