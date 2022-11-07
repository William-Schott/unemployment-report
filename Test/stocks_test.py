##test file must be _test.py
## test function must me test_...

def test_usd_formatting():


  
#make sure that this is indented from the def
    from App.stocks import format_usd
    from pandas import DataFrame




    assert format_usd(4.5) == "$4.50"

        ## the following two lines are edge cases
    assert format_usd(4.555555) == "$4.56"

    assert format_usd(1234567890 == "$1,234,567,890.00")

    def test_data_fetching():
        result = fetch_stocks_data("NFLX")
        assert isinstance(result,DataFrame)
        assert "timestamp" in result.columns
        assert"adjusted_close" in result.columns
        assert "high" in result.columns
        assert "low" in result.columns

        assert len(result) >= 100