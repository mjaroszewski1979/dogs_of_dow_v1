# Import TestClient from FastAPI to simulate HTTP requests in tests
from fastapi.testclient import TestClient
# Import the FastAPI application instance from the main module
from main import app

# Create a TestClient instance for the FastAPI app
# This client will be used to simulate HTTP requests to the app's endpoints during testing
client = TestClient(app)

def test_app_exists():
    """
    Test to ensure that the application instance exists.
    This verifies that the app is properly initialized.
    """
    assert app != None

def test_index_get():
    """
    Test the GET request to the index page.
    This method checks if the index page loads correctly with the expected status code and content.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>MJ TRADING - HOME</title>' in response.text 
   
def test_about():
    """
    Test the GET request to the about page.
    This method checks if the about page loads correctly with the expected status code and content.
    """
    response = client.get("/about")
    assert response.status_code == 200
    assert '<title>MJ TRADING - ABOUT</title>' in response.text 

def test_index_post():
    """
    Test the POST request to the index page.
    This method checks if the form works correctly given valid email and password, verifying the response status and content.
    """
    response = client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    assert response.status_code == 200
    assert 'THANK YOU MJ@GMAIL.COM FOR REGISTERING!' in response.text

def test_signals_failure():
    """
    Test the behavior of the signals page with invalid credentials.
    This method checks the response status and content when incorrect credentials are provided.
    """
    client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    response = client.get('/signals', auth=('wrong@gmail.com', 'wrong'))
    assert response.status_code == 401
    assert '{"detail":"Incorrect email or password"}' in response.text

def test_signals_success():
    """
    Test the behavior of the signals page with correct credentials.
    This method checks the response status and content when correct credentials are provided.
    """
    client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    response = client.get('/signals', auth=('mj@gmail.com', 'maciej'))
    assert response.status_code == 200
    assert '<title>MJ TRADING - SIGNALS</title>' in response.text 






   
