import pandas_datareader as pdr
import datetime
from threading import Thread
from fastapi.security import HTTPBasicCredentials
from werkzeug.security import check_password_hash
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic


security = HTTPBasic()


class DowDogs:
    def __init__(self, start = datetime.datetime(2020, 1, 1), end = datetime.datetime.now(), period=125):
        self.start = start
        self.end = end
        self. period = period

        self. results = []
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

        self.data = pdr.get_data_yahoo(symbol, self.start, self.end)
        total = []
        nums = range(2, 252)
        for num in nums:
            if self.data['Adj Close'][-1] > self.data['Adj Close'][-num]:
                result = 1
            else:
                result = -1
            total.append(result)
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
        if result not in self.results:
            self.results.append(result)
            self.results.sort(key=lambda x: x[1])

    def get_trend(self):

        threads = []

        for ticker in self.tickers:
            threads.append(Thread(target=self.get_data, args=[ticker]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        return self.results

class User:
    def __init__ (self):
        self.users = {'email': [], 'pass_hash': []}


    def get_current_username(self, credentials: HTTPBasicCredentials = Depends(security)):


        usr_email = credentials.username
        usr_pass = credentials.password


        if usr_email in self.users['email']:
            item = self.users['email'].index(usr_email)
            pass_hash = self.users['pass_hash'][item]


            result = check_password_hash(pass_hash, usr_pass)
            if result == True:
                return credentials.username


            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Basic"},)


        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect email or password",
                    headers={"WWW-Authenticate": "Basic"},)
