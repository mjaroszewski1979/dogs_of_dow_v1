# Import pandas_datareader for fetching financial data
import pandas_datareader as pdr
# Import datetime for handling date and time
import datetime
# Import Thread for multi-threading
from threading import Thread
# Import HTTPBasicCredentials for security
from fastapi.security import HTTPBasicCredentials
# Import check_password_hash for password verification
from werkzeug.security import check_password_hash
# Import FastAPI dependencies and exceptions
from fastapi import Depends, HTTPException, status
# Import HTTPBasic for HTTP basic authentication
from fastapi.security import HTTPBasic

# Initialize HTTP basic security
security = HTTPBasic()

# Define the DowDogs class to manage top Dow Jones stocks
class DowDogs:
    """
    Initialize the DowDogs class with default start and end dates, and a period.
    This sets up initial attributes, including start and end dates, period, results, markets, and tickers.
    """
    def __init__(self, start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), period=125):
        self.start = start
        self.end = end
        self. period = period

        self. results = []
        
        # Define the names and tickers of the Dogs of the Dow companies
        self.markets = {
            'MMM' : '3M',
            'AMGN' : 'AMGEN',
            'CVX' : 'CHEVRON',
            'CSCO' : 'CISCO SYSTEMS',
            'KO' : 'COCA COLA',
            'DOW' : 'DOW',
            'IBM' : 'IBM',
            'MRK' : 'MERCK',
            'VZ' : 'VERIZON',
            'WBA' : 'WALGREENS BOOTS'
      
        }
        self.tickers = ['MMM', 'AMGN', 'CVX', 'CSCO', 'KO', 'DOW', 'IBM', 'MRK', 'VZ', 'WBA']

    def get_data(self, symbol):
        """
        Fetch data using the Yahoo Finance API to establish the current trend for a given symbol.
        This method calculates the trend score based on the comparison of the most recent data point to the prices over the past year.
        """

        self.data = pdr.get_data_yahoo(symbol, self.start, self.end)
        total = []
        nums = range(2, 252)
        
        # Compare the most recent data point to the prices from 2 to 252 days ago
        for num in nums:
            if self.data['Adj Close'][-1] > self.data['Adj Close'][-num]:
                result = 1
            else:
                result = -1
            total.append(result)
            
        # Calculate the total score
        total = (sum(total))
        
        if total > self.period:
            score = 'STRONG BUY'
        elif total > 0 and total < self.period:
            score = 'BUY'
        elif total < 0 and total > -self.period:
            score = 'SELL'
        elif total < -self.period:
            score = 'STRONG SELL'
        else:
            score = 'FLAT'
            
        result = [score, self.markets[symbol]]
        
        # Check for existing result and update results list
        if result not in self.results:
            self.results.append(result)
            self.results.sort(key=lambda x: x[1])

    def get_trend(self):
        """
        Assign each use of the Yahoo Finance API to an individual thread to fetch data concurrently.
        This method starts threads for each ticker and returns the results for all stocks.
        """

        threads = []

        for ticker in self.tickers:
            threads.append(Thread(target=self.get_data, args=[ticker]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        # Return the results for all stocks
        return self.results

# Define the User class to manage user credentials
class User:
    """
    Initialize the User class with an empty users dictionary to store email and password hashes.
    """
    def __init__ (self):
        self.users = {'email': [], 'pass_hash': []}

    def get_current_username(self, credentials: HTTPBasicCredentials = Depends(security)):
        """
        Get the current user's username using HTTPBasicCredentials and validate the credentials.
        This method checks the provided email and password, raising an exception if they are incorrect.
        """

        usr_email = credentials.username
        usr_pass = credentials.password

        # Check for existing record
        if usr_email in self.users['email']:
            item = self.users['email'].index(usr_email)
            pass_hash = self.users['pass_hash'][item]

            # Verify the provided password matches the stored password hash
            result = check_password_hash(pass_hash, usr_pass)
            if result == True:
                return credentials.username

            # Raise an exception if the password is incorrect
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},)

        # Raise an exception if the email is incorrect
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Basic"},)
