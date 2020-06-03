import task

def test_1_1():
    assert task.hello() == "Hello, World!"

def test_1_2():
    assert task.add(2, 3) == 5
    assert task.add(-2, 3) == 1
    assert task.add("Hello, ", "World!") == "Hello, World!"
