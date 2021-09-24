import fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form, Depends
from starlette.requests import Request
from werkzeug.security import generate_password_hash
from utilities import DowDogs, User

# Pointing to correct folder for html templates
templates = Jinja2Templates('templates')


router = fastapi.APIRouter()


dow_dog = DowDogs()
trend = dow_dog.get_trend()

dow_user = User()




@router.get("/")
def index_get(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


@router.post("/")
def index_post(request: Request, email: str = Form(...), password: str = Form(...)):

    # Checking for existing email address
    if email not in dow_user.users['email']:

        try:
            
            # Generating password hash 
            pass_hash = generate_password_hash(password)
            
            # Saving user credentials
            dow_user.users['pass_hash'].append(pass_hash)
            dow_user.users['email'].append(email)
            
            return templates.TemplateResponse('index.html', context={'request': request, 'pass_hash': pass_hash, 'email': email.upper()})

        except KeyError:
            msg = 'WROND PASSWORD!'
            return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
        
    # Flashing error message when encountering email address duplication
    else:
        msg = 'SORRY, THAT EMAIL ALREADY EXISTS IN OUR DATABASE!'
        return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
    



@router.get("/signals")
def read_current_user(request: Request, username: str = Depends(dow_user.get_current_username)):
    msg = 'CONNECTION ERROR. PLEASE TRY AGAIN LATER.'
    
    # Checking for correct number of results
    try:
        return templates.TemplateResponse('signals.html', context={'request': request, 'trend': trend})
    except:
        len(trend) < 10
        return templates.TemplateResponse("index.html", {'request': request, 'msg': msg})

@router.get("/about")
def about_get(request: Request):
    return templates.TemplateResponse('about.html', context={'request': request})


