import pandas_datareader as pdr
import datetime
from threading import Thread
from fastapi.security import HTTPBasicCredentials
from werkzeug.security import check_password_hash
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic


security = HTTPBasic()

# Creating base class for top dow jones stocks
class DowDogs:
    def __init__(self, start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), period=125):
        self.start = start
        self.end = end
        self. period = period

        self. results = []
        
        # Dogs of dow companies names and associated tickers
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

    # Fetching data using Yahoo Finance API to establish current trend for a given symbol 
    def get_data(self, symbol):

        self.data = pdr.get_data_yahoo(symbol, self.start, self.end)
        total = []
        nums = range(2, 252)
        
        # Comparing most recent data point to price ranging from 2 to 252 days ( trading year )
        for num in nums:
            if self.data['Adj Close'][-1] > self.data['Adj Close'][-num]:
                result = 1
            else:
                result = -1
            total.append(result)
            
        # Getting a total score
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
        
        # Checking for existing result
        if result not in self.results:
            self.results.append(result)
            self.results.sort(key=lambda x: x[1])

    # Assigning each use of Yahoo Finance API to individual thread 
    def get_trend(self):

        threads = []

        for ticker in self.tickers:
            threads.append(Thread(target=self.get_data, args=[ticker]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        # Returning results for all stocks
        return self.results

# Creating user class with basic credentials - username and password
class User:
    def __init__ (self):
        self.users = {'email': [], 'pass_hash': []}

    # Getting current user credentials using HTTPBasicCredentials and HTTPBasic
    def get_current_username(self, credentials: HTTPBasicCredentials = Depends(security)):


        usr_email = credentials.username
        usr_pass = credentials.password

        # Checking for existing record
        if usr_email in self.users['email']:
            item = self.users['email'].index(usr_email)
            pass_hash = self.users['pass_hash'][item]

            # Ensuring that provided password match stored password hash
            result = check_password_hash(pass_hash, usr_pass)
            if result == True:
                return credentials.username

            # Raising an exception when password is incorrect
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},)

        # Raising an exception when provided email is incorrect
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Basic"},)
