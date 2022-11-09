##test file must be _test.py
## test function must me test_...




  
#make sure that this is indented from the def

from app.stocks import format_usd, fetch_stocks_data

from pandas import DataFrame





def test_usd_formatting():
    from app.stocks import format_usd, fetch_stocks_data
    from pandas import DataFrame


    assert format_usd(4.5) == "$4.50"

    assert format_usd(4.5555555) == "$4.56"

    assert format_usd(1234567890) == "$1,234,567,890.00"

    #assert format_usd("OOPS") == "______"



def test_data_fetching():
    result = fetch_stocks_data("NFLX")
    assert isinstance(result, DataFrame)

    assert "timestamp" in result.columns
    assert "adjusted_close" in result.columns
    assert "high" in result.columns
    assert "low" in result.columns


    assert len(result) >= 100    ##test invalid inputs?
   ### result = fetch_stocks_data("NFLX")
