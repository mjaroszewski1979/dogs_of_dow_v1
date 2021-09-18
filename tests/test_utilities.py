from utilities import DowDogs, User
import pytest

dow_dog = DowDogs()
dow_user = User()

# Ensures that attributes of DowDogs class exists
@pytest.mark.parametrize("dow_dog_attributes, unexpected_result", [
    (dow_dog.start, None),
    (dow_dog.end, None),
    (dow_dog.period, None),
    (dow_dog.results, None),
    (dow_dog.markets, None),
    (dow_dog.tickers, None)
])
def test_dow_dog_attributes(dow_dog_attributes, unexpected_result):
    assert dow_dog_attributes != unexpected_result

# Ensures that get trend method works correctly
def test_get_trend():
    data = dow_dog.get_trend()
    result = ['SELL', '3M']
    assert result in data

# Ensures that get data method works correctly
def test_get_data():
    dow_dog.get_data('MMM')
    result = ['SELL', '3M']
    assert result in dow_dog.results

# Ensures that attribute of User class exists
def test_dow_user():
    assert dow_user.users != None

