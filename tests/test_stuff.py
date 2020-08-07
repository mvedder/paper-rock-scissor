from stuff import hello_world, two_fer


def test_hello_world():
    actual = hello_world()
    expected = "hello world"

    assert expected == actual


def test_2fer_matthew():
    assert "One for Matthew, one for me." == two_fer("Matthew") # f(2) = 4


def test_2fer_daniel():
    assert "One for Daniel, one for me." == two_fer("Daniel") # f(3) = 6
