## Project Requirements Document for Dogs of Dow

## Unit Tests

### Application Initialization Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The application must be properly initialized. | When the application instance is created. | The application instance (app) should not be None. | test_app_exists

### Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The index view must handle GET requests correctly. | When a GET request is made to the index URL (/). | The response should have a status code of 200. The response must contain the text <title>MJ TRADING - HOME</title>. | test_index_get
The index view must handle POST requests correctly. | When a POST request is made to the index URL (/) with valid email and password. | The response should have a status code of 200.  The response must contain the text THANK YOU <email> FOR REGISTERING!. | test_index_post

### About View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The about view must handle GET requests correctly. | When a GET request is made to the about URL (/about). | The response should have a status code of 200. The response must contain the text <title>MJ TRADING - ABOUT</title>. | test_about

### Signals View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The signals view must handle GET requests with authentication correctly. | When a GET request is made to the signals URL (/signals) with incorrect credentials. | The response should have a status code of 401. The response must contain the text {"detail":"Incorrect email or password"}. | test_signals_failure
The signals view must handle GET requests with authentication correctly. | When a GET request is made to the signals URL (/signals) with correct credentials. | The response should have a status code of 200. The response must contain the text <title>MJ TRADING - SIGNALS</title>. | test_signals_success

### DowDogs Class Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The DowDogs class must have specific attributes correctly initialized. | When checking the attributes start, end, period, results, markets, and tickers of an instance of DowDogs. | Each of these attributes should not be None. | test_dow_dog_attributes
The get_trend method of the DowDogs class must return the expected data. | When the get_trend method is called on an instance of DowDogs. | The method should return data containing the list with values <signal>, <ticker>. | test_get_trend
The get_data method of the DowDogs class must update the results attribute correctly. | When the get_data method is called on an instance of DowDogs with the argument <ticker>. | The results attribute should contain the list with values <signal>, <ticker>. | test_get_data

### User Class Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The User class must have the users attribute correctly initialized. | When checking the users attribute of an instance of User. | The users attribute should not be None. | test_dow_user

## Selenium Tests

### Home Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The home page must display the correct title. | When the home page is accessed. | The title of the page should be "MJ TRADING - HOME". | is_title_matches
The About link on the home page must navigate to the About page correctly. | When the About link is clicked from the home page. | The title of the page should change to "MJ TRADING - ABOUT". | is_about_link_works
The Home link on the About page must navigate back to the home page correctly. | When the Home link is clicked from the About page. | The title of the page should change back to "MJ TRADING - HOME". | is_home_link_works
The registration form on the home page must work correctly with valid inputs. | When the registration form is submitted with a valid email and password. | The registration should be successful, and a success message should appear. The success message should contain the text "THANK YOU <email> FOR REGISTERING!". | is_register_form_works
The Signals link on the home page must navigate to the Signals page correctly. | When the Signals link is clicked from the home page. | The page should navigate to the Signals page. | click_signals_link

### About Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The About page must display the correct title. | When the About page is accessed. | The title of the page should be "MJ TRADING - ABOUT". | is_title_matches
The About page must display the correct heading. | When the About page is accessed. | The heading of the page should be displayed correctly. The heading should contain the text "DOGS OF THE DOW IS AN INVESTMENT STRATEGY THAT ATTEMPTS TO BEAT THE DOW JONES". | is_about_heading_displayed

### Signals Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Signals page must display the correct title. | When the Signals page is accessed. | The title of the page should be "MJ TRADING - SIGNALS". | is_signals_title_matches







 

