##test file must be _test.py
## test function must me test_...

def test_usd_formatting():


  

from app.stocks import format_usd


assert format_usd(4.5) == "$4.50"

## the following two lines are edge cases
assert format_usd(4.555555) == "$4.56"

assert format_usd(1234567890 == "$1,234,567,890.00")


