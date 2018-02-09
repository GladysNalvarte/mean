from workshop_assert_new import mean
# checking the definition and the behaviour of the code
def test_ints():
    num_list = [1,2,3,4,5]
    obs = mean(num_list)
    exp = 3
    assert obs == exp
    
def test_double():
    num_list = [1,2,3,4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp
    
def test_long():
    big = 100000000
    obs = mean(range(1,big))
    exp = big/2.0
    assert obs == exp
    
def test_complex():
    #testing for complex numbers
    #as arithmetic mean of complex numbers
    num_list = [2 + 3j, 3+4j, -32 -2j]
    obs = mean(num_list)
    exp = NotImplemented
    assert obs == exp