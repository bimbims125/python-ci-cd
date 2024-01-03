from main import add_numbers, divide_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5

def test_dividing():
  result = divide_numbers(20, 5)
  assert result == 5
