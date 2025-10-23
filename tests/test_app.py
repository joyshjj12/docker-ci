from app import add

def run_tests():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0