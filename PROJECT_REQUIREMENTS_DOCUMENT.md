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





 

