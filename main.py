# Import the FastAPI module
import fastapi
# Import StaticFiles to serve static files
from fastapi.staticfiles import StaticFiles
# Import the views module containing API route definitions
import views

# Create an instance of the FastAPI application
app = fastapi.FastAPI()

# Mount the static files directory
# This serves static files from the "static" directory at the "/static" URL path
app.mount("/static", StaticFiles(directory="static"), name="static")

def configure():
    """
    Add each APIRouter from the views module to the main FastAPI application.
    This function includes all the routes defined in the views.router.
    """
    app.include_router(views.router)

# Call the configure function to include the routes
configure()
