# Import FastAPI for creating APIs
import fastapi
# Import Jinja2Templates for template rendering
from fastapi.templating import Jinja2Templates
# Import FastAPI dependencies
from fastapi import Request, Form, Depends
# Import Request from Starlette for HTTP requests
from starlette.requests import Request
# Import generate_password_hash for password hashing
from werkzeug.security import generate_password_hash
# Import DowDogs and User classes from utilities module
from utilities import DowDogs, User

# Point to the folder containing HTML templates
templates = Jinja2Templates('templates')

# Create an APIRouter instance for routing endpoints
router = fastapi.APIRouter()

# Initialize instances of DowDogs and User classes
dow_dog = DowDogs()
trend = dow_dog.get_trend()
dow_user = User()

@router.get("/")
def index_get(request: Request):
    """
    Handle GET request to the index page.
    Render the 'index.html' template with the request context.
    """
    return templates.TemplateResponse('index.html', context={'request': request})


@router.post("/")
def index_post(request: Request, email: str = Form(...), password: str = Form(...)):
    """
    Handle POST request to the index page.
    This method checks if the email already exists in the database,
    generates a password hash, and saves the user credentials.
    It renders the 'index.html' template with appropriate messages based on the outcome.
    """

    # Check if the email already exists
    if email not in dow_user.users['email']:

        try:
            # Generate password hash
            pass_hash = generate_password_hash(password)
            
            # Save user credentials
            dow_user.users['pass_hash'].append(pass_hash)
            dow_user.users['email'].append(email)
            
            return templates.TemplateResponse('index.html', context={'request': request, 'pass_hash': pass_hash, 'email': email.upper()})

        except KeyError:
            msg = 'WROND PASSWORD!'
            return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
        
    # Flash error message when encountering email address duplication
    else:
        msg = 'SORRY, THAT EMAIL ALREADY EXISTS IN OUR DATABASE!'
        return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
    

@router.get("/signals")
def read_current_user(request: Request, username: str = Depends(dow_user.get_current_username)):
    """
    Handle GET request to the signals page.
    This method checks the current user's username and renders the 'signals.html' template with trend data.
    If there are less than 10 results, it renders the 'index.html' template with an error message.
    """
    msg = 'CONNECTION ERROR. PLEASE TRY AGAIN LATER.'
    
    try:
        return templates.TemplateResponse('signals.html', context={'request': request, 'trend': trend})
    except:
        len(trend) < 10
        return templates.TemplateResponse("index.html", {'request': request, 'msg': msg})

@router.get("/about")
def about_get(request: Request):
    """
    Handle GET request to the about page.
    Render the 'about.html' template with the request context.
    """
    return templates.TemplateResponse('about.html', context={'request': request})


