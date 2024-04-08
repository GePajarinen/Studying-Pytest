from hello import more_hello


def test_more_hello():
    assert "Hi" == more_hello()


# test to fail:
def test_tofail_more_hello():
  assert "Bye" == more_hello()
  