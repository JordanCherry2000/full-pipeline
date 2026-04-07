def test_math():
    assert 1 + 1 == 2


def test_pandas_import():
    import pandas as pd

    df = pd.DataFrame({"a": [1, 2]})
    assert not df.empty
