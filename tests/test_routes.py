from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

# Ensures that the application instance exists
def test_app_exists():
    assert app != None

# Ensures that index page loads correctly
def test_index_get():
    response = client.get("/")
    assert response.status_code == 200
    assert '<title>MJ TRADING - HOME</title>' in response.text 
   
# Ensures that about page loads correctly
def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert '<title>MJ TRADING - ABOUT</title>' in response.text 

# Ensures that form works correctly given valid email and password
def test_index_post():
    response = client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    assert response.status_code == 200
    assert 'THANK YOU MJ@GMAIL.COM FOR REGISTERING!' in response.text

# Ensures that signals page behaves as expected given invalid credentials
def test_signals_failure():
    client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    response = client.get('/signals', auth=('wrong@gmail.com', 'wrong'))
    assert response.status_code == 401
    assert '{"detail":"Incorrect email or password"}' in response.text

# Ensures that signals page behaves as expected given correct credentials
def test_signals_success():
    client.post('/', data = dict(email='mj@gmail.com', password='maciej'))
    response = client.get('/signals', auth=('mj@gmail.com', 'maciej'))
    assert response.status_code == 200
    assert '<title>MJ TRADING - SIGNALS</title>' in response.text 






   