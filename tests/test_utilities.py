# Import pytest for writing and running tests
import pytest
# Import DowDogs and User classes from the utilities module
from utilities import DowDogs, User

# Create instances of DowDogs and User for testing
dow_dog = DowDogs()
dow_user = User()


@pytest.mark.parametrize("dow_dog_attributes, unexpected_result", [
    (dow_dog.start, None),
    (dow_dog.end, None),
    (dow_dog.period, None),
    (dow_dog.results, None),
    (dow_dog.markets, None),
    (dow_dog.tickers, None)
])
def test_dow_dog_attributes(dow_dog_attributes, unexpected_result):
    """
    Test to ensure that attributes of the DowDogs class exist.
    This verifies that specific attributes are not None.
    """
    assert dow_dog_attributes != unexpected_result

def test_get_trend():
    """
    Test the get_trend method of the DowDogs class.
    This method checks if the get_trend method returns the expected data.
    """
    data = dow_dog.get_trend()
    result = ['SELL', '3M']
    assert result in data

def test_get_data():
    """
    Test the get_data method of the DowDogs class.
    This method checks if the get_data method works correctly and updates the results attribute.
    """
    dow_dog.get_data('MMM')
    result = ['SELL', '3M']
    assert result in dow_dog.results

def test_dow_user():
    """
    Test to ensure that the users attribute of the User class exists.
    This verifies that the users attribute is not None.
    """
    assert dow_user.users != None

