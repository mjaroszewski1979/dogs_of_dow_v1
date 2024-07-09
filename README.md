## Dogs of Dow
### This is an application built with FastAPI, one of the fastest Python web frameworks. It is designed to display current trend directions for the top 10 high-yield dividend members of the Dow Jones Industrial Index. The application fetches data from Yahoo Finance and uses it to analyze trends and make recommendations.

### Features
* Data Validation and Conversion: Ensures data integrity through path operation functions (request handlers).
* User Authentication: Uses get_current_user function and HTTPBasicCredentials authentication scheme.
* Password Hashing: Utilizes Werkzeug Security for hashing passwords and verifying correctness.
* Error Handling: Employs HTTPException from FastAPI to raise exceptions for incorrect credentials.
* Template Rendering: Leverages Jinja2Templates to render specific HTML templates for dynamic content presentation.
* Minification: Reduces webpage loading speed with advanced HTML and CSS minification.
* Background Data Fetching: Moves data fetching to a background thread to avoid delays.

### Installation

1. Clone the repository
  ```bash
  git clone https://github.com/mjaroszewski1979/dogs_of_dow_v1.git
  cd dogs_of_dow_v1
  ```
2. Create a Virtual Environment
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
1. Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```
4. Start the Server
  ```bash
  uvicorn main:app --reload
  ```

### Usage
Access the application by opening your browser and going to http://127.0.0.1:8000/. The application will display trend directions based on the fetched data.

### Testing

1. Run Unit Tests
  ```bash
  pytest
  ```
2. Run Selenium Tests
  ```bash
  coverage run -p pytest tests_selenium
  ```
3. Combine and Generate Coverage Report
  ```bash
  coverage combine
  coverage html
  ```

### Code Coverage

<img src="https://github.com/mjaroszewski1979/dogs_of_dow_v1/blob/main/cov_report.png">

### Docker

1. Pull the Image
  ```bash
  docker pull <imagename>
  ```
2. Create and Start a Container
  ```bash
  docker run -p 8000:8000 <imagename>
  ```
3. Or use a .env file:
  ```bash
  docker run -p 8000:8000 --env-file .env <imagename>
  ```

### Technologies Used
* FastAPI: Web framework for building the application.
* Selenium: For automated browser testing.
* Yahoo Finance API: For fetching financial data.
* Docker: Containerization of the application.
  
### Contributing
* Fork the repository.
* Create a new branch: git checkout -b feature-branch.
* Make your changes and commit them: git commit -m 'Add new feature'.
* Push to the branch: git push origin feature-branch.
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)



   ![caption](https://github.com/mjaroszewski1979/dogs_of_dow_v1/blob/main/dogs_mockup.png)

 Code | Docker | Technologies
 ---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/dogs_of_dow_v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/dogs_of_dow) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/fastapi_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pandas.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/numpy_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/jinja_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/uvicorn_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png">  <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> 
