from stuff import hello_world, two_fer


def test_hello_world():
    actual = hello_world()
    expected = "hello world"

    assert expected == actual


def test_2fer_matthew():
    assert "One for Matthew, one for me." == two_fer("Matthew")
#
#
# def test_2fer_daniel():
#     actual = two_fer("Daniel")
#     expected = "One for Daniel, one for me."
#
#     assert expected == actual
