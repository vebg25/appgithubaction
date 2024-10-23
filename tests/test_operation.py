from src.math_operation import add,subtract

def test_add():
  assert add(2,3)==5
  assert add(1,-1)==0

def test_subtract():
  assert subtract(3,-3)==0
  assert subtract(1,3)==-2