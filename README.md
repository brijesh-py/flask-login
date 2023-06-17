# Flask User Authentication

This is a Flask application with user authentication using Flask-Login. It allows users to register, login, and view a home page.

#### Login
![Screenshot from 2023-06-17 14-08-56](https://github.com/brijesh-py/flask-login/assets/134686367/39c9b037-65f4-46ef-9cc7-5ed92cdc85af)

#### Join
![Screenshot from 2023-06-17 14-09-18](https://github.com/brijesh-py/flask-login/assets/134686367/6a68c79b-b2a2-43e5-93a9-615175628935)


#### Home
![Screenshot from 2023-06-17 14-09-41](https://github.com/brijesh-py/flask-login/assets/134686367/43ced19f-54a2-46b5-a261-24916de02914)


## Installation

1. Clone the repository:

git clone https://github.com/brijesh-py/flask-login.git

2. Install the dependencies:

pip install -r requirements.txt

3. Run the application:

python app.py

## Usage

1. Open your web browser and go to `http://localhost:5000`.
2. You will see the home page, where you can register or login.
3. After logging in, you will be redirected to the home page, where you can see a welcome message.

## Project Structure

The project structure is as follows:
.
├── app.py
├── models.py
├── urls.py
├── views.py
├── templates
│   ├── index.html
│   ├── join.html
│   └── login.html
├── static
│   └── <static_files>
└── db.sqlite3


- `app.py`: Initializes the Flask application and runs it.
- `models.py`: Defines the user model and database schema.
- `urls.py`: Defines the URL routes for the application.
- `views.py`: Contains the view functions for handling HTTP requests.
- `templates/`: Contains the HTML templates for rendering the pages.
- `static/`: Contains static files such as CSS stylesheets and images.
- `db.sqlite3`: SQLite database file for storing user information.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors
Brijesh GP brijeshsoftdev@duck.com
### Thanks for visiting here.
